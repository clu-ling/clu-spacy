import spacy
from doc_to_doc import DocToCluDoc
from processors.ds import Document as CluDocument # FIXME
from processors.ds import Sentence
import unittest

PIPELINE = "en_core_web_sm"

class TestDocToCluDoc(unittest.TestCase):    
    """
        Create a SpaCy document instance on a test text.
        Test DocToCluDoc class on test SpaCy doc.
    """
    nlp = spacy.load(PIPELINE)
    text = "I was reading the paper."
    doc = nlp(text)

    def test_doc_to_doc(self):
        cludoc = DocToCluDoc(doc).cluDoc
        assert isinstance(cludoc, CluDocument)

    # Check equivalence of SpaCy and CluDocument attributes (e.g. word_list = word_list)