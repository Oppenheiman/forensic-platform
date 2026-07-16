
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class ContradictionDetector(BaseForensicAgent):
    def investigate(self):
        # Find TODO / FIXME / HACK contradicting implementation
        cmd = ["rg", "-n", "TODO|FIXME|HACK", "--no-heading"]
        if self.subsystem: cmd.append(self.subsystem)
        else: cmd.append(".")
        
        result = self.run_cmd(cmd).splitlines()
        if result:
            self.add_evidence("TechDebt_Markers", f"Found {len(result)} TODO/FIXME markers", Confidence.CERTAIN)
