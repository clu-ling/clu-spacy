from dataclasses import dataclass

@dataclass(frozen=True)
class AppInfo:
    """
    General information about the application.
    """
    version: str = "0.1"
    description: str = "Processors-spacy is a library for converting between SpaCy Doc and processors Document instances."
    author: str = "zwellington"
    contact: str = "gus@parsertongue.org"
    repo: str = "https://github.com/clu-ling/processors-spacy"
    license: str = "None" # FIXME: Get license
    
    @property
    def download_url(self) -> str: 
      return f"{self.repo}/archive/v{self.version}.zip"
    

info = AppInfo()