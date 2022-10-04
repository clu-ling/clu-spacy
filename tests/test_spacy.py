import spacy
from clu.spacy.utils import ConverterUtils as converter

# from clu.spacy.annotator import SpacyProcessor
from processors.ds import Document as CluDocument  # FIXME
from processors.ds import Sentence
from spacy.tokens import Doc as SpacyDocument
import unittest
import os

DEFAULT_PIPELINE = "en_core_web_trf"


class TestConverterUtils(unittest.TestCase):
    """
    Create a SpaCy document instance on a test text.
    Test DocToCluDoc class on test SpaCy doc.
    """

    nlp = spacy.load(DEFAULT_PIPELINE)
    # text = "The huskies howled all night."
    # test_spacy_doc = nlp(text)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_clu_doc = os.path.join(dir_path, 'cluDoc1.json')

    def test_tutorial(self):
        """TestConverterUtils.test_tutorial() should run the tutorial without errors."""
        text = "I saw the boy with a telescope."
        spacy_doc = self.nlp(text)

        # Convert the SpaCy Doc to a Clu Document
        clu_doc = converter.to_clu_doc(spacy_doc)

        self.assertIsInstance(clu_doc, CluDocument)

    # # FIXME: Add Tests for to_spacy_doc() with update.
    # def test_to_spacy_doc(self):
    #     spacydoc = converter.to_spacy_doc(self.test_clu_doc)
    #     assert isinstance(spacydoc, SpacyDocument)

    # def test_to_clu_doc(self):
    #     cludoc = converter.to_clu_doc(self.test_spacy_doc)
    #     # spacydoc_words = []
    #     # spacydoc_lemmas = []
    #     # for token in self.test_clu_doc:
    #     #     spacydoc_words.append(token.text)
    #     #     spacydoc_lemmas.append(token.lemma)

    #     # assert isinstance(cludoc, CluDocument)
    #     # assert cludoc.text == self.test_spacy_doc.text
    #     # assert len(cludoc.words) == len(spacydoc_words)
    #     # assert cludoc.lemmas == spacydoc_lemmas
    #     pass

    # def test_make_sentence(self):
    #     pass

    # def test_spaces_to_offsets(self):
    #     pass

    # def test_dep_to_graph(self):
    #     pass
