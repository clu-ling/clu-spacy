from typing import Optional
from fastapi import FastAPI, File

from spacy.tokens import Doc as SpacyDoc
from processors.ds import Document as CluDocument

from processorspacy.utils import ConverterUtils as converter

server = FastAPI()

@server.post("/api/to-clu-doc")
def to_clu_doc(spacyDoc: SpacyDoc):
    cluDoc = converter.to_clu_doc(spacyDoc)
    return cluDoc.to_JSON

# FIXME: Implement to_spacy_doc request