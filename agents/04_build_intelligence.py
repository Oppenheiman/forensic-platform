
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class BuildIntelligenceAgent(BaseForensicAgent):
    def investigate(self):
        build_files = {
            "BUILD.gn": "GN (Chromium)",
            "Makefile": "Make",
            "CMakeLists.txt": "CMake",
            "Kconfig": "Kconfig (Kernel)"
        }
        
        for filename, tool in build_files.items():
            cmd = ["git", "ls-files", filename]
            result = self.run_cmd(cmd).strip()
            if result:
                count = len(result.splitlines())
                self.add_evidence(f"BuildSystem_{tool}", f"Found {count} {filename} files", Confidence.CERTAIN)
