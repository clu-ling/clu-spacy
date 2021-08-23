
from typing import Text

from processors.annotators import Processor

from processors.ds import Document as CluDocument
import spacy
from clu.spacy.utils import ConverterUtils as converter

DEFAULT_PIPELINE = "en_core_web_sm"

class SpacyProcessor(Processor):

    def __init__(self, pipeline = DEFAULT_PIPELINE):
        self.pipeline = pipeline
        self.nlp = spacy.load(self.pipeline)

    def annotate(self, text: Text) -> CluDocument:        
        doc = self.nlp(text)
        cluDoc = converter.to_clu_doc(doc)

        return cluDoc