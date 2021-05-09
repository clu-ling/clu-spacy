
from typing import Sequence, List, Tuple, Dict
import spacy
from spacy.tokens import Doc as SpacyDoc
from spacy.tokens import Span
from processors.ds import Document as CluDocument
from processors.ds import Sentence


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

        to_spacyDoc : 

        to_cluDoc :

    """

    @staticmethod
    def to_spacy_doc(cluDoc: CluDocument): # -> SpacyDoc:
        """Create a Doc object.
                vocab (Vocab): A vocabulary object, which must match any models you
                    want to use (e.g. tokenizer, parser, entity recognizer).
                words (Optional[List[str]]): A list of unicode strings to add to the document
                    as words. If `None`, defaults to empty list.
                spaces (Optional[List[bool]]): A list of boolean values, of the same length as
                    words. True means that the word is followed by a space, False means
                    it is not. If `None`, defaults to `[True]*len(words)`
                user_data (dict or None): Optional extra data to attach to the Doc.
                tags (Optional[List[str]]): A list of unicode strings, of the same
                    length as words, to assign as token.tag. Defaults to None.
                pos (Optional[List[str]]): A list of unicode strings, of the same
                    length as words, to assign as token.pos. Defaults to None.
                morphs (Optional[List[str]]): A list of unicode strings, of the same
                    length as words, to assign as token.morph. Defaults to None.
                lemmas (Optional[List[str]]): A list of unicode strings, of the same
                    length as words, to assign as token.lemma. Defaults to None.
                heads (Optional[List[int]]): A list of values, of the same length as
                    words, to assign as heads. Head indices are the position of the
                    head in the doc. Defaults to None.
                deps (Optional[List[str]]): A list of unicode strings, of the same
                    length as words, to assign as token.dep. Defaults to None.
                sent_starts (Optional[List[Union[bool, None]]]): A list of values, of
                    the same length as words, to assign as token.is_sent_start. Will be
                    overridden by heads if heads is provided. Defaults to None.
                ents (Optional[List[str]]): A list of unicode strings, of the same
                    length as words, as IOB tags to assign as token.ent_iob and
                    token.ent_type. Defaults to None.
        """
        # Doc.from_bytes
        #doc_data = {"Create Doc object":}
        #doc = SpacyDoc(**doc_data)
        pass


    @staticmethod
    def to_clu_doc(spacyDoc: SpacyDoc) -> CluDocument:
        """
            Converts a SpacyDoc : Sequence[Token] to a CluDocument : Sequence[Sentence]

            Parameters: spacyDoc, a SpacyDoc object

            Returns - a CluDocument object
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

            Parameters: sent, a SpaCy Span object

            Returns: sentence, a processors Sentence object
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
    def make_graphs(sent: Span) -> Dict:
        graphs = dict()

        # {graph-name -> {edges: [{source, destination, relation}], roots: [int]}}

        return graphs
