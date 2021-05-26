
from typing import Sequence, List, Tuple, Dict, Union, Iterable
import spacy
from spacy.tokens import Doc as SpacyDoc
from spacy.tokens import Span, Token
from processors.ds import Document as CluDocument
from processors.ds import Sentence

DEFAULT_PIPELINE = "en_core_web_sm"

class ConverterUtils:

    """
        A collection of utlity methods for coverting between SpaCy Doc and processor Document containers.

        Supported Containers
        --------------------
        SpaCy Doc : Sequence[Token]
                A sequence of SpaCy Token objects.

        CluDocument : Sequence[Sentence]
                A sequence of processor Setence objects.

        Methods
        -------
        to_clu_doc(spacyDoc)
            Converts a SpaCy Doc object to a processors Document object

        to_spacy_doc(cluDoc, pipeline)
            Converts a processors Document object to a SpaCy Doc object 
    """

    @staticmethod
    def to_clu_doc(spacyDoc: SpacyDoc) -> CluDocument:
        """
            Converts a SpacyDoc: Sequence[Token] to a CluDocument: Sequence[Sentence]

            Parameters
            ----------
            spacyDoc: a SpacyDoc object

            Returns
            -------
            A CluDocument object
        """
        sentences = [] #Initialize List[Sentence]

        for sent in spacyDoc.sents:
            sentences.append(ConverterUtils.make_sentence(sent))

        doc = CluDocument(sentences)
        
        return doc

    @staticmethod
    def to_spacy_doc(cluDoc: Union[CluDocument, str], pipeline = DEFAULT_PIPELINE) -> SpacyDoc:
        """
           Converts a CluDocument: Sequence[Sentence] to a SpacyDoc: Sequence[Token]

           Parameters
           ----------
           cluDoc: a processor Document object or path to JSON
           pipeline: spacy pipeline, for vocab object

           Returns
           -------
           A SpacyDocument object
        """
        if isinstance(cluDoc, str):
            with open(cluDoc, 'r') as f:
                cluDoc = CluDocument.load_from_JSON(f.read())
        
        nlp = spacy.load(pipeline)

        doc_data = ConverterUtils.make_data(cluDoc)        
        doc = SpacyDoc(nlp.vocab, **doc_data)

        return doc

    ### Helper Methods :

    @staticmethod
    def make_sentence(sent: Span) -> Sentence:
        """
            Converts a SpaCy Span (Doc slice) object to a processors Sentence object.

            Parameters
            ----------
            sent: a SpaCy Span object

            Returns
            -------
            sentence: a processors Sentence object
        """

        startoffsets, endoffsets = ConverterUtils.spaces_to_offsets(sent)

        params = {
            "text": sent.text,
            "words": [token.text for token in sent],
            "startOffsets": startoffsets,
            "endOffsets": endoffsets,
            "tags": [token.tag_ for token in sent],
            "lemmas": [token.lemma_ for token in sent],
            "chunks": ["O" for token in sent], # FIXME: SpaCy noun_chunks?
            "entities": [t.ent_iob_+"-"+t.ent_type_ if t.ent_type_ != "" else "O" for t in sent],
            "graphs": ConverterUtils.dep_to_graph(sent)
        }

        sentence = Sentence(**params)

        return sentence

    @staticmethod
    def make_data(cluDoc: CluDocument) -> Dict:
        """
            Converts a CluDocument object to a dictionary of Doc attributes.

            Parameters
            ----------
            cluDoc: a processors Document object

            Returns
            -------
            data: a dictionary of SpaCy Doc attributes
        """
        spaces = []
        for sent in cluDoc.sentences:
            spaces += ConverterUtils.offsets_to_spaces(sent)
        # assert len(spaces) == len(cluDoc.words)

        heads, deps = ConverterUtils.graph_to_dep(cluDoc)

        data = {
            "words": cluDoc.words,
            "spaces": ConverterUtils.offsets_to_spaces(cluDoc),
            "tags": cluDoc.tags,
            "lemmas": cluDoc.lemmas,
            "heads": heads,
            "deps": deps,
            "ents": cluDoc._entities
        }
        return data

    @staticmethod
    def spaces_to_offsets(sent: Span) -> Tuple[List[int]]:

        startOffSets = list()
        endOffSets = list()

        for token in sent:
            offset = token.idx - sent.start_char
            startOffSets.append(offset)
            endOffSets.append(offset + len(token.text))

        assert startOffSets[0] == 0

        return (startOffSets, endOffSets)

    @staticmethod
    def offsets_to_spaces(cluDoc: CluDocument) -> List[bool]:
        # FIXME 
        spaces = []
        # for sent in cluDoc.sentences:
        return spaces

    @staticmethod
    def dep_to_graph(sent: Span) -> Dict:
        graphs = dict()
        # {graph-name: {edges: [{source: int, destination: int, relation: str}], roots: [int]}}

        spacy_graph = dict()

        edges = []
        for token in sent:
            children = token.children
            child = ConverterUtils.peek(children)
            while child is not None:
                edge = {"source": token.i-sent.start, "destination": child.i-sent.start, "relation": child.dep_}
                edges.append(edge)
                child = ConverterUtils.peek(children)

        spacy_graph["edges"] = edges
        spacy_graph["roots"] = [sent.root.i-sent.start]

        graphs["stanford-basic"] = spacy_graph

        return graphs    

    @staticmethod
    def graph_to_dep(cluDoc: CluDocument) -> Tuple[List, List]:
        # FIXME
        heads = []
        deps = []
        return (heads, deps)

    @staticmethod
    def peek(generator: Iterable) -> Union[Token, None]:
        """peek() will return either the next Token in the iterable or None."""
        try:
            first = next(generator)
        except StopIteration:
            return None
        return first