# Training a Pipeline FAQ

## What kind of data structure is supported?

In training a pipeline through the `spacy train` command, data must be in either `.conllu` or `.iob` format. These formats are then converted to binary in the `.spacy` format for training.

## Can I use custom models?

Yes, spaCy allows for easy integration of custom models in training. You can use custom models in both built-in and custom components. In the config file this would be defined under the `components.ner.model` block (ner is an example component here), and the python code would be attached via the `--code` override in the `spacy train` command.
