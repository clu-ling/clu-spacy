
from typing import Sequence, List, Tuple, Dict, Union
import spacy
from spacy.tokens import Doc as SpacyDoc
from spacy.tokens import Span
from processors.ds import Document as CluDocument
from processors.ds import Sentence

PIPELINE = "en_core_web_sm"

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
        to_spacy_doc(cluDoc, pipeline)
            Converts a processors Document object to a SpaCy Doc object

        to_clu_doc(spacyDoc)
            Converts a SpaCy Doc object to a processors Document object

    """

    @staticmethod
    def to_spacy_doc(cluDoc: Union[CluDocument, str], pipeline = PIPELINE) -> SpacyDoc:
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
        sents = list(spacyDoc.sents)
        assert isinstance(sents, List)

        sentences = [] #Initialize List[Sentence]
        for sent in sents:
            sentences.append(ConverterUtils.make_Sentence(sent))

        doc = CluDocument(sentences)
        
        return doc


    @staticmethod
    def make_Sentence(sent: Span) -> Sentence:
        """
            Converts a SpaCy Span (Doc slice) object to a processors Sentence object.

            Parameters
            ----------
            sent: a SpaCy Span object

            Returns
            -------
            sentence: a processors Sentence object
        """

        offsets = ConverterUtils.find_offsets(sent)

        params = {
            "text": sent.text,
            "words": [token.text for token in sent],
            "startOffsets": offsets[0],
            "endOffsets": offsets[1],
            "tags": [token.pos for token in sent],
            "lemmas": [token.lemma for token in sent],
            "chunks": ["O" for token in sent], # FIXME: SpaCy noun_chunks?,
            "entities": [token.ent_iob_+token.ent_type_ for token in sent],
            "graphs": ConverterUtils.make_graphs(sent)
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

        heads, deps = ConverterUtils.parse_graphs(cluDoc)

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
    def find_offsets(sent: Span) -> Tuple[List[int]]: # FIXME: Some offsets not accurate.
        startOffSets = [0] #The first start offset is always zero.
        running = sent[0].text_with_ws
        endOffSets = [len(running)-1]

        for i in range(len(sent)-1):
            startOffSets.append(len(running))
            running += sent[i+1].text_with_ws
            endOffSets.append(len(running)-1)

        return (startOffSets, endOffSets)

    @staticmethod
    def offsets_to_spaces(cluDoc: CluDocument) -> List[bool]:
        # FIXME 
        spaces = []
        # for sent in cluDoc.sentences:
        return spaces

    @staticmethod
    def make_graphs(sent: Span) -> Dict:
        graphs = dict()

        # {graph-name -> {edges: [{source, destination, relation}], roots: [int]}}

        return graphs    

    @staticmethod
    def parse_graphs(cluDoc: CluDocument) -> Tuple[List, List]:
        # FIXME
        heads = []
        deps = []
        return (heads, deps)