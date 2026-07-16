
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class GitArchaeologyAgent(BaseForensicAgent):
    def investigate(self):
        # Find most active authors (ownership)
        cmd = ["git", "log", "--format='%aN'"]
        if self.subsystem: cmd.extend(["--", self.subsystem])
        
        result = self.run_cmd(cmd)
        authors = {}
        for line in result.splitlines():
            line = line.strip().strip("'")
            if line:
                authors[line] = authors.get(line, 0) + 1
                
        for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True)[:5]:
            self.add_evidence(f"Owner_{author}", f"Authored {count} commits", Confidence.LIKELY)
            
        # Find bug hotspots
        cmd = ["git", "log", "--oneline", "--grep=bug", "--name-only"]
        if self.subsystem: cmd.extend(["--", self.subsystem])
        result = self.run_cmd(cmd)
        files = {}
        for line in result.splitlines():
            if not line.startswith(" ") and "/" in line:
                files[line] = files.get(line, 0) + 1
                
        for f, count in sorted(files.items(), key=lambda x: x[1], reverse=True)[:5]:
            self.add_evidence(f"BugHotspot_{f}", f"Appeared in {count} bugfix commits", Confidence.LIKELY)
