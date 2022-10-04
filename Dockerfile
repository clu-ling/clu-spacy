FROM parsertongue/python:3.8

LABEL author="Gus Hahn-Powell"
LABEL description="Image definition for Python-based clu-spacy."

# Create app directory
WORKDIR /app

# Install python dependencies
RUN pip install -U pip setuptools wheel

# iPython
RUN pip install -U ipython==7.19.0 \
    jupyter==1.0.0 \
    jupyter-contrib-nbextensions==0.5.1 && \
    jupyter contrib nbextension install --user &&\
    pytest==5.3.4


# Rust for tokenizers
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN rustc --version
RUN pip install -U setuptools_rust

# SpaCy
RUN pip install -U "spacy"

# SpaCy trained pipe
RUN python -m spacy download en_core_web_trf
    
# Bundle app source
COPY . .

# Move scripts to local/bin
RUN mv scripts/* /usr/local/bin/ && \
    chmod u+x /usr/local/bin/test-all && \
    rmdir scripts

# Assignment-specific deps
RUN pip install -e ".[all]"

RUN pip install -U markupsafe==2.0.1
# CMD ["ipython"]
# Launch jupyter
# CMD ["/bin/bash", "/usr/local/bin/launch-notebook.sh"]
# Launch api
# CMD ["uvicorn", "processors_extensions:spacy:api", "--reload", "--port", "8000", "--host", "0.0.0.0"]
CMD ["/bin/bash", "api", "--config", "/app/tests/test-config.yml"]