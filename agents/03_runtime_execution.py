
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class RuntimeExecutionAgent(BaseForensicAgent):
    def investigate(self):
        # Find entry points
        patterns = [
            (r"int\s+main\s*\(", "C_Main"),
            (r"MODULE_INIT\(", "Kernel_Module_Init"),
            (r"wmain\s*\(", "Windows_Main")
        ]
        
        for regex, desc in patterns:
            cmd = ["rg", "-l", "--no-heading", regex]
            if self.subsystem: cmd.append(self.subsystem)
            else: cmd.append(".")
            
            result = self.run_cmd(cmd).strip()
            if result:
                files = result.splitlines()
                self.add_evidence(f"Entrypoint_{desc}", f"Found in {len(files)} files. Example: {files[0]}", Confidence.CERTAIN)
