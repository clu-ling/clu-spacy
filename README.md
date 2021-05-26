# processors_extensions

```processors-extensions``` is a python library with extension modules for the ```py-processors``` library. 

Currently, only the ```spacy``` extension is available. This extension provides support for ```SpaCy```, allowing users to create processors ```Document```s with annotations from SpaCy. This allows for the use of annotations from custom trained SpaCy pipelines.

# Build

```docker build -f Dockerfile -t parsertongue/processorsextensions:latest .```

# API

```docker run -it -p 8888:8000 parsertongue/processorsextensions:latest api --config /app/bin/test-config.yml```

Open your browser to [localhost:8888/docs](http://localhost:8888/docs).

# TEST

```docker run -it -v $PWD:/app parsertongue/processorextensions:latest test-all```
