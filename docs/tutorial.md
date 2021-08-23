# Converting SpaCy Doc and Clu Documents

The `clu-spacy` library can be used as methods in a python script. The following shows how to import the converter and use it:

```python
import spacy
# Import the converter utilities
from clu.spacy.utils import ConverterUtils as converter

# Load a SpaCy Doc object
nlp = spacy.load('en_core_web_sm')
doc = nlp('The jets flew overhead.')

# Convert the SpaCy Doc to a Clu Document
cludoc = converter.to_clu_doc(doc)

# Convert the Clu Document back to a SpaCy Doc
spacydoc = converter.to_spacy_doc(cludoc)

# This spacydoc should be the same as the original doc
assert len(spacydoc) == len(doc)
```

## Training a Pipeline

See [Training](./training.md) for a tutorial on using the `clu-spacy` library to train a SpaCy pipeline.
