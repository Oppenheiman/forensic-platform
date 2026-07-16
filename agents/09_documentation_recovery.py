
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence
from pathlib import Path

class DocumentationRecoveryAgent(BaseForensicAgent):
    def investigate(self):
        report_path = self.repo_path / "CLAUDE.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# Architecture Recovery Report\n\n")
            f.write(f"## Repository: `{self.repo_path}`\n")
            f.write(f"## Subsystem: `{self.subsystem or 'Full Repo'}\n\n")
            
            f.write("## Evidence Graph Summary\n\n")
            
            # Group findings by agent
            agents = {}
            for edge in self.graph.edges:
                if edge["relation"] == "has_finding":
                    agent = edge["provenance"]
                    node = self.graph.nodes[edge["target"]]
                    if agent not in agents: agents[agent] = []
                    agents[agent].append(node)
                    
            for agent, nodes in agents.items():
                f.write(f"### {agent}\n")
                for node in nodes:
                    attrs = node["attrs"]
                    f.write(f"- **[{node['type']}] {attrs.get('subject', 'N/A')}**: {attrs.get('detail', '')}\n")
                f.write("\n")
                
        self.add_evidence("Documentation", f"Generated {report_path.name}", Confidence.CERTAIN)
