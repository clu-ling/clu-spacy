from typing import List, Text
import os


class AppInfo:
    """
    General information about the application.
    """

    version: Text = "0.2"
    commit: Text = os.environ.get("GIT_COMMIT", "unknown")
    description: Text = "spacy is a module for converting between SpaCy Doc and processors Document instances."
    authors: List[Text] = ["myedibleenso", "zwellington"]
    contact: Text = "gus@parsertongue.org"
    repo: Text = "https://github.com/clu-ling/clu-spacy"
    license: Text = "Apache 2.0"

    @property
    def download_url(self) -> Text:
        return f"{self.repo}/archive/v{self.version}.zip"


info = AppInfo()
