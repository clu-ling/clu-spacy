# Training

## Training from command line

https://spacy.io/usage/training#config

`spacy init fill-config base-config.cfg config.cfg`

### Component Options

### Config options

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
