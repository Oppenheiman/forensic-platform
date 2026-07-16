
import subprocess
from pathlib import Path
from .evidence_graph import EvidenceGraph, Confidence

class BaseForensicAgent:
    def __init__(self, repo_path, graph: EvidenceGraph, subsystem=None):
        self.repo_path = Path(repo_path).resolve()
        self.graph = graph
        self.subsystem = subsystem
        self.name = self.__class__.__name__
        
        # Root node for this repository
        self.repo_node_id = str(self.repo_path)
        self.graph.add_node(self.repo_node_id, "Repository", {"path": str(self.repo_path)})
        
    def run_cmd(self, cmd):
        try:
            result = subprocess.run(
                cmd, cwd=self.repo_path, capture_output=True, text=True, check=True, timeout=60
            )
            return result.stdout
        except Exception:
            return ""
            
    def add_evidence(self, subject, evidence_detail, confidence: Confidence, node_type="Finding"):
        """Helper to add simple evidence nodes linked to the repo."""
        node_id = f"{self.name}_{subject}"
        self.graph.add_node(node_id, node_type, {"subject": subject, "detail": evidence_detail})
        self.graph.add_edge(self.repo_node_id, node_id, "has_finding", self.name, confidence, evidence_detail)
