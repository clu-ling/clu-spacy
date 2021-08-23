# Installation

## Anaconda

`clu-spacy` is written for **Python >= v3.8**.  One option to develop is to install all virtual environment (ex. `conda`, `venv`, `poetry`, etc.).  Using `conda`, the library can be installed interactively with a compatible environment using the following commands:

```bash
conda create --name clu-spacy python=3.8 ipython
source activate clu-spacy
# execute the following command from the project root:
pip install -e ".[dev]"
```

`[dev]` will include dependencies for running tests and generating the documentation.


## Docker

For those familiar with Docker, another option is to use a container with bind mounts as a development environment.  Note that the instructions below assume you're developing using a Linux-based environment (they've also been tested on MacOS Catalina).

First, you'll need to build the docker image:

```bash
docker build -f Dockerfile -t "parsertongue/clu-spacy:latest" .
```

Launch a container using this image and connect to it:

```bash
docker run -it -v $PWD:/app "parsertongue/clu-spacy:latest /bin/bash"
```

Thanks to the bind mount, changes made to files locally (i.e., outside of the container) will be reflected inside the running container.  The `parsertongue/clu-spacy` includes Jupyter and iPython:

```bash
ipython
```

```python
from clu.spacy.utils import ConverterUtils

converter = ConverterUtils()
```

### Removing old docker containers, images, etc.

If you want to save some space on your machine by removing images and containers you're no longer using, [see the instructions here](https://docs.docker.com/config/pruning/).  As always, use caution when deleting things.
