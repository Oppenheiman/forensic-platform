
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class ConfigurationAgent(BaseForensicAgent):
    def investigate(self):
        # Sample feature flags / config macros
        cmd = ["rg", "--no-filename", "-o", r"#ifdef\s+(\w+)", "-r", "$1"]
        if self.subsystem: cmd.append(self.subsystem)
        else: cmd.append(".")
        
        result = self.run_cmd(cmd)
        flags = {}
        for line in result.splitlines():
            line = line.strip()
            if line:
                flags[line] = flags.get(line, 0) + 1
                
        for flag, count in sorted(flags.items(), key=lambda x: x[1], reverse=True)[:10]:
            self.add_evidence(f"FeatureFlag_{flag}", f"Used {count} times in #ifdef", Confidence.CERTAIN)
            self.graph.add_node(flag, "ConfigurationFlag")
            self.graph.add_edge(flag, self.repo_node_id, "alters_behavior_of", self.name, Confidence.LIKELY)
