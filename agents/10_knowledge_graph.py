
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class KnowledgeGraphAgent(BaseForensicAgent):
    def investigate(self):
        # Export graph to JSON
        filepath = self.repo_path / "knowledge_graph.json"
        self.graph.export_json(filepath)
        self.add_evidence("KnowledgeGraph", f"Exported CPG to {filepath.name}", Confidence.CERTAIN)
