# Training

The following methods for training a spaCy pipeline are based on the [spaCy documentation](https://spacy.io/usage/training).

## Training Data

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

## Training from command line

A spaCy pipeline can be trained via the command line using a config.cfg file. The `config.cfg` can be generated in one of two ways:

- [init method](https://spacy.io/api/cli#init-config): `python -m spacy init config config.cfg [options]`
- manually: You can use spaCy's [quickstart](https://spacy.io/usage/training#quickstart) and `init fill-config`

After the appropriate config.cfg is generated (see [here](# FIXME: gist) for an example config), run the following:

`python -m spacy train config.cfg --output ./output/path [options]`

If the paths to the train and dev data are not included in the config.cfg, inclue the tags `--paths.train ./train --paths.dev ./dev`.

This will automatically launch a training sequence for the specified number of epochs and settings in the config. The output directory will be populated with a `best` and `last` model.

### Component Options

You can use the included spaCy factory components or add custom components with `nlp.add_pipe()`. When using the factory components the user can specify which model to use. These models are `Thinc` models used by spaCy. Custom components can also make use of these models or can include custom coded models. This code can be attached to the trained pipeline when packaged.

Built-in components are ([spaCy](https://spacy.io/usage/processing-pipelines#built-in)):

- DependencyParser
- EntityLinker
- EntityRecognizer
- Morphologizer
- SentenceRecognizer
- SpanCategorizer
- Tagger
- TextCategorizer
- Tok2Vec

These components can be trained with custom architecture or using the default architectures by spaCy. When using the default architectures, using the config quickstart will autofill for this option.

### Config options

For further details on the options available to the `config.cfg` see the [spaCy docs](https://spacy.io/usage/training#config).

## Training from script

`Language.to_disk()` after `Language.add_pipe()`, create_pipe() deprecated.

## Adding custom components

https://spacy.io/api/language#component

```python
@Language.component("my_component")
def my_component(doc):
    # do soemthing to doc
    return doc
```

The new `my_component` can now be added to the pipeline via `Language.add_pipe("my_component")`. (Language.create_pipe() is now deprecated for user use).

## Saving and loading the pipeline

### spacy train

Specify output directory, run `spacy package /pipeline /output`.

### Language.to_disK()

After modifying Language object, run `Language.to_disk("/path/to/pipeline")` then `spacy package /pipeline /output`.

## FAQ

Mutliple training data files passed to `spacy train`? NER data vs Conllu data? (DocBin().merge? Can add NER attr to conllu docbins.)
