
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class APISurfaceAgent(BaseForensicAgent):
    def investigate(self):
        # Look for exported symbols (Linux Kernel / C++)
        patterns = [
            (r"EXPORT_SYMBOL_GPL\(([a-zA-Z0-9_]+)\)", "Kernel_Exported_API"),
            (r"__attribute__\(\(visibility\(\"default\"\)\)\)", "Linux_CLib_Export")
        ]
        
        for regex, desc in patterns:
            cmd = ["rg", "--no-filename", "-o", regex, "-r", "$1"]
            if self.subsystem: cmd.append(self.subsystem)
            else: cmd.append(".")
            
            result = self.run_cmd(cmd).strip()
            if result:
                symbols = list(set(result.splitlines()))[:10]
                for sym in symbols:
                    self.graph.add_node(sym, "PublicAPI")
                    self.graph.add_edge(self.repo_node_id, sym, "exports_api", self.name, Confidence.CERTAIN)
