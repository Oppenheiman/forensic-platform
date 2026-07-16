
import argparse
import sys
import os

# Add path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.evidence_graph import EvidenceGraph
from agents import (
    01_repository_archaeologist,
    02_architecture_recovery,
    03_runtime_execution,
    04_build_intelligence,
    05_api_surface,
    06_configuration,
    07_dependency,
    08_git_archaeology,
    09_documentation_recovery,
    10_knowledge_graph,
    11_pattern_recognition,
    12_llm_investigation,
    13_contradiction_detector,
    14_architecture_drift,
    15_runtime_evidence_fusion
)

# Fix module names starting with numbers (invalid Python identifiers)
RepoArch = 01_repository_archaeologist.RepositoryArchaeologist
ArchRec = 02_architecture_recovery.ArchitectureRecoveryAgent
RunExec = 03_runtime_execution.RuntimeExecutionAgent
BuildInt = 04_build_intelligence.BuildIntelligenceAgent
APISurf = 05_api_surface.APISurfaceAgent
Config = 06_configuration.ConfigurationAgent
Dep = 07_dependency.DependencyAgent
GitArch = 08_git_archaeology.GitArchaeologyAgent
DocRec = 09_documentation_recovery.DocumentationRecoveryAgent
KnowGraph = 10_knowledge_graph.KnowledgeGraphAgent
PatRec = 11_pattern_recognition.PatternRecognitionAgent
LLMInv = 12_llm_investigation.LLMInvestigationAgent
ContraDet = 13_contradiction_detector.ContradictionDetector
ArchDrift = 14_architecture_drift.ArchitectureDriftAgent
RunFusion = 15_runtime_evidence_fusion.RuntimeEvidenceFusion

AGENTS = [RepoArch, ArchRec, RunExec, BuildInt, APISurf, Config, Dep, GitArch, PatRec, LLMInv, ContraDet, ArchDrift, KnowGraph, DocRec, RunFusion]

def main():
    parser = argparse.ArgumentParser(description="Forensic Investigation Platform")
    parser.add_argument("repo_path", help="Path to repository")
    parser.add_argument("--subsystem", help="Target subsystem", default=None)
    args = parser.parse_args()
    
    print(f"[*] Initializing Forensic Platform on {args.repo_path}")
    graph = EvidenceGraph()
    
    for AgentClass in AGENTS:
        print(f"[*] Running {AgentClass.__name__}...")
        agent = AgentClass(args.repo_path, graph, args.subsystem)
        agent.investigate()
        
    print("[*] Investigation complete. Review CLAUDE.md and knowledge_graph.json")

if __name__ == "__main__":
    main()
