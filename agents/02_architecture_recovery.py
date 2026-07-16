
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence
import os

class ArchitectureRecoveryAgent(BaseForensicAgent):
    def investigate(self):
        # Reconstruct layers based on folder structure
        cmd = ["git", "ls-files"]
        if self.subsystem: cmd.append(self.subsystem)
        files = self.run_cmd(cmd).splitlines()
        
        layers = {"ui": 0, "controller": 0, "domain": 0, "infrastructure": 0, "browser": 0, "renderer": 0, "ipc": 0, "gpu": 0, "os": 0}
        for f in files:
            for layer in layers:
                if f"//{layer}/" in f or f"/{layer}/" in f:
                    layers[layer] += 1
                    
        for layer, count in layers.items():
            if count > 0:
                self.add_evidence(f"Layer_{layer}", f"Found {count} files in {layer} directory", Confidence.LIKELY)
                self.graph.add_node(f"Layer_{layer}", "ArchitecturalLayer")
                self.graph.add_edge(self.repo_node_id, f"Layer_{layer}", "contains_layer", self.name, Confidence.LIKELY)
