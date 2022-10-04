# Converting SpaCy Doc and Clu Documents

The `clu-spacy` library can be used as methods in a python script. The following shows how to import the converter and use it:

```bash
# download a spacy model
spacy download en_core_web_trf
```

```python
import spacy
# Import the converter utilities
from clu.spacy.utils import ConverterUtils as converter

# Load SpaCy pipeline
nlp = spacy.load("en_core_web_trf")

# Create a SpaCy Doc.
text = "I saw the boy with a telescope."
spacy_doc = nlp(text)

# Convert the SpaCy Doc to a Clu Document
clu_doc = converter.to_clu_doc(spacy_doc)

assert isinstance(clu_doc, CluDocument)
```

## Training a Pipeline

See [Training](./training.md) for a tutorial on using the `clu-spacy` library to train a SpaCy pipeline.
