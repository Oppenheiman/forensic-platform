
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class ArchitectureDriftAgent(BaseForensicAgent):
    def investigate(self):
        # Check if UI directly accesses DB (Drift)
        cmd = ["rg", "-l", "SELECT.*FROM", "ui/"]
        if self.subsystem: cmd = ["rg", "-l", "SELECT.*FROM", self.subsystem]
        
        result = self.run_cmd(cmd).strip()
        if result:
            self.add_evidence("Architecture_Drift", "UI layer directly contains SQL queries", Confidence.HYPOTHESIS)
