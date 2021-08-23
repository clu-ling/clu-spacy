# Training Data

As of spaCy v3.0 the main method in training a custom NLP pipeline is the `spacy train` command. This method requires data in the spaCy binary format which is serialized with the `.spacy` extension. There are conversion utilities developed by spaCy for `.conllu`, `.iob`, and `.json` formats. (The `.json` format is used in spaCy v2.0). 

The `clu-spacy` library also provides utility methods for converting data and checking tokenization of the custom data against the `spaCy blank lang`. Using the command `convert-data` on custom CoNLL and IOB data will produce match files and offer some retokenization. Run the following command within the data directory:

```bash
docker ...
```

When the data is not in CoNLL format the user must define the DocBin object manually. This can be accomplished with some preprocessing code, for example (from [spaCy documentation](https://spacy.io/usage/training#training-data), annotated):

```python
import spacy
# The DocBin oject is used for serializing data for training.
from spacy.tokens import DocBin

# A blank Language object is a pipeline with no components.
nlp = spacy.blank("en")

training_data = [
  ("Tokyo Tower is 333m tall.", [(0, 11, "BUILDING")]),
]

# the DocBin will store the example documents
db = DocBin()
for text, annotations in training_data:
    # Create doc object for text, tokenization defined by base language ("en")
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
```
