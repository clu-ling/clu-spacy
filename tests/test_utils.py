import spacy
from processorspacy.utils import ConverterUtils as converter
from processors.ds import Document as CluDocument # FIXME
from processors.ds import Sentence
from spacy.tokens import Doc as SpacyDocument
import unittest
import os

PIPELINE = "en_core_web_sm"

class TestConverterUtils(unittest.TestCase):    
    """
        Create a SpaCy document instance on a test text.
        Test DocToCluDoc class on test SpaCy doc.
    """
    nlp = spacy.load(PIPELINE)
    text = "The huskies howled all night."
    test_spacy_doc = nlp(text)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_clu_doc = os.path.join(dir_path, 'cluDoc1.json')

    def test_to_spacy_doc(self):
        spacydoc = converter.to_spacy_doc(test_clu_doc)
        assert isinstance(spacydoc, SpacyDocument)

    def test_to_clu_doc(self):
        cludoc = converter.to_clu_doc(test_spacy_doc)
        assert isinstance(cludoc, CluDocument)

    # Check equivalence of SpaCy and CluDocument attributes (e.g. word_list = word_list)