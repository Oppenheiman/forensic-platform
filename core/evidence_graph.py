
import json
from enum import Enum

class Confidence(str, Enum):
    CERTAIN = "Certain"
    LIKELY = "Likely"
    HYPOTHESIS = "Hypothesis"
    UNKNOWN = "Unknown"

class EvidenceGraph:
    """
    Core Code Property Graph (CPG).
    Instead of a flat list of findings, all observations become nodes and edges.
    Higher-level conclusions are inferred from the graph topology.
    """
    def __init__(self):
        self.nodes = {}
        self.edges = []
        
    def add_node(self, node_id, node_type, attrs=None):
        if node_id not in self.nodes:
            self.nodes[node_id] = {"type": node_type, "attrs": attrs or {}}
            
    def add_edge(self, source, target, relation, provenance, confidence, detail=""):
        self.edges.append({
            "source": source,
            "target": target,
            "relation": relation,
            "provenance": provenance,
            "confidence": confidence.value if isinstance(confidence, Confidence) else confidence,
            "detail": detail
        })
        
    def export_json(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({"nodes": self.nodes, "edges": self.edges}, f, indent=2)
            
    def get_edges_by_relation(self, relation):
        return [e for e in self.edges if e["relation"] == relation]
