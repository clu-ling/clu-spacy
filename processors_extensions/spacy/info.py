from pydantic import BaseModel

class AppInfo(BaseModel):
    """
    General information about the application.
    """
    version: str = "0.1"
    description: str = "spacy is a module for converting between SpaCy Doc and processors Document instances."
    author: str = "zwellington"
    contact: str = "gus@parsertongue.org"
    repo: str = "https://github.com/clu-ling/processors-spacy"
    license: str = "Apache 2.0"
    
    @property
    def download_url(self) -> str: 
      return f"{self.repo}/archive/v{self.version}.zip"
    

info = AppInfo()