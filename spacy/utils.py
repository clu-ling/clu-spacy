class ConverterUtils:

    @staticmethod
    def to_spacy_doc():
        # Doc.from_bytes
        pass

    @staticmethod
    def to_clu_doc():
        pass



# import spacy
# from typing import Sequence, List
# from processors.ds import Document as CluDocument
# from processors.ds import Sentence

# # FIXME: Implement SpaCy Token type object?

# class DocToCluDoc(object):

#     """
#         A conversion class for generating CluDocuments from SpaCy Docs.

#         Parameters
#         ----------
#         doc : SpaCy Doc object -> Sequence[Token]

#         Attributes
#         ----------
#         spacyDoc :  Sequence[Token]
#                 The original SpaCy Doc object.

#         sentences : List[Sentence]
#                 A list of Sentence objects.

#         cluDoc : CluDocument
#             A CluDocument object generated from the spacyDoc object.
     
#     """

#     def __init__(self, doc):
#         # FIXME: fix init definitions
#         self.spacyDoc = self.doc
#         self.sentences = self._generate_sentences(self.spacyDoc)
#         self.cluDoc = CluDocument(self.sentences)

#     def _generate_sentences(self, spacyDoc) -> List[Sentence]:
#         """
#             Sentence Parameters
#             ---------
#             text : str or None
#                 The text of the `Sentence`.
#             words : [str]
#                 A list of the `Sentence`'s tokens.
#             startOffsets : [int]
#                 The character offsets starting each token (inclusive).
#             endOffsets : [int]
#                 The character offsets marking the end of each token (exclusive).
#             tags : [str]
#                 A list of the `Sentence`'s tokens represented using part of speech (PoS) tags.
#             lemmas : [str]
#                 A list of the `Sentence`'s tokens represented using lemmas.
#             chunks : [str]
#                 A list of the `Sentence`'s tokens represented using IOB-style phrase labels (ex. `B-NP`, `I-NP`, `B-VP`, etc.).
#             entities : [str]
#                 A list of the `Sentence`'s tokens represented using IOB-style named entity (NE) labels.
#             graphs : dict
#                 A dictionary of {graph-name -> {edges: [{source, destination, relation}], roots: [int]}}
#         """
        
#         sentences = []

#         # Iterate over the spacyDoc sentences (Span -> Doc[a:b]: Sequence[Token])
#         for sent in spacyDoc.sents:

#             #Initialize the params dict passed to Sentence(**kwargs)
#             params = {
#                 "text": None,
#                 "words": [],
#                 "startOffsets": [],
#                 "endOffsets": [],
#                 "tags": [],
#                 "lemmas": [],
#                 "chunks": [],
#                 "entities": [],
#                 "graphs": {}
#             }

#             params["text"] = sent.text
#             params["words"] = [token.text for token in sent]
#             params["startOffsets"] = None # FIXME
#             params["endOffsets"] = None # FIXME
#             params["tags"] = [token.pos for token in sent] # token.pos or token.tag?
#             params["lemmas"] = [token.lemma for token in sent]
#             params["chunks"] = ["O" for token in sent] # FIXME: SpaCy noun_chunks?
#             params["entities"]: List[str] = [token.ent_iob_+token.ent_type_ for token in sent]
#             params["graphs"] = None # FIXME

#             sentences.append(Sentence(**params))

#         return sentences