
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence
import os

class PatternRecognitionAgent(BaseForensicAgent):
    def investigate(self):
        # Detect architectural patterns based on folder structure
        cmd = ["git", "ls-files"]
        if self.subsystem: cmd.append(self.subsystem)
        files = self.run_cmd(cmd).splitlines()
        
        patterns = {
            "MVC": ["model", "view", "controller"],
            "DDD": ["domain", "application", "infrastructure"],
            "Layered": ["ui", "service", "repository", "database"]
        }
        
        for pattern, keywords in patterns.items():
            found = {kw: False for kw in keywords}
            for f in files:
                for kw in keywords:
                    if f"/{kw}/" in f:
                        found[kw] = True
            if all(found.values()):
                self.add_evidence(f"Pattern_{pattern}", f"Detected {pattern} structure", Confidence.LIKELY)
