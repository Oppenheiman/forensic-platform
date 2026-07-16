
from core.base_agent import BaseForensicAgent
from core.evidence_graph import Confidence

class RepositoryArchaeologist(BaseForensicAgent):
    def investigate(self):
        # Discover languages
        cmd = ["git", "ls-files"]
        if self.subsystem: cmd.append(self.subsystem)
        files = self.run_cmd(cmd).splitlines()
        
        exts = {}
        for f in files:
            ext = f.split('.')[-1] if '.' in f else 'none'
            exts[ext] = exts.get(ext, 0) + 1
            
        for ext, count in sorted(exts.items(), key=lambda x: x[1], reverse=True)[:5]:
            self.add_evidence(f"Language_{ext}", f"Found {count} files with .{ext}", Confidence.CERTAIN)
            
        # Discover submodules
        if self.run_cmd(["cat", ".gitmodules"]):
            self.add_evidence("Submodules", "Repository uses git submodules", Confidence.CERTAIN)
