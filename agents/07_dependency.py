
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class DependencyAgent(BaseForensicAgent):
    def investigate(self):
        cmd = ["rg", "--no-filename", "-o", r"#include\s+[\"<](.*?)[\">]", "-r", "$1"]
        if self.subsystem: cmd.append(self.subsystem)
        else: cmd.append(".")
        
        result = self.run_cmd(cmd)
        include_counts = {}
        for line in result.splitlines():
            line = line.strip()
            if line:
                include_counts[line] = include_counts.get(line, 0) + 1
                
        for dep, count in sorted(include_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
            self.graph.add_node(dep, "Module")
            self.graph.add_edge(dep, self.repo_node_id, "high_fan_in_dependency", self.name, Confidence.CERTAIN, f"Included {count} times")
