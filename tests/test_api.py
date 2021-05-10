import spacy
from fastapi.testclient import TestClient
from processorspacy import api

from processorspacy.utils import ConverterUtils as converter

from spacy.tokens import Doc as SpacyDocument
from processors.ds import Document as CluDocument

import unittest
import requests

PIPELINE = "en_core_web_sm"

class TestAPI(unittest.TestCase):

    client = TestClient(api)

    nlp = spacy.load(PIPELINE)
    text = "I was reading the paper."
    test_spacy_doc = nlp(text)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_clu_doc = os.path.join(dir_path, 'cluDoc1.json')

    def test_to_clu_doc(self):
        """
            /api/to-clu-doc should return a processors Document.
        """
        response = self.client.get("/api/to-clu-doc", self.test_spacy_doc)
        print(response.status_code)
        print(type(response.status_code))
        assert response.status_code == 200
        cluDoc = CluDocument.load_from_JSON(response)
        assert isinstance(cluDoc, CluDocument)

    def test_to_spacy_doc(self):
        response = self.client.get("/api/to-spacy-doc", self.test_clu_doc)
        print(response.status_code)
        print(type(response.status_code))
        assert response.status_code == 200
        spacyDoc = response
        assert isinstance(spacyDoc, SpacyDocument)
