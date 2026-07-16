
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class LLMInvestigationAgent(BaseForensicAgent):
    def investigate(self):
        # Generate hypotheses for LLM investigation based on low-confidence edges
        prompts = []
        for edge in self.graph.edges:
            if edge["confidence"] == Confidence.LIKELY.value and edge["relation"] == "high_fan_in_dependency":
                prompts.append(f"Investigate why module {edge['source']} has high fan-in. Is it a core domain concept or a leaky abstraction?")
                
        if prompts:
            self.add_evidence("LLM_Prompts", f"Generated {len(prompts)} investigation prompts for LLM", Confidence.CERTAIN)
