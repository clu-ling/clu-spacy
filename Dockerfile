FROM python:3.8

LABEL author="Zachary Wellington"
LABEL description="Image definition for Python-based clu-spacy."

# Create app directory
WORKDIR /app

# Install python dependencies
RUN pip install -U pip==21.1.1 setuptools==56.2.0 wheel==0.36.2

# iPython
RUN pip install -U ipython==7.19.0 \
    jupyter==1.0.0 \
    jupyter-contrib-nbextensions==0.5.1 && \
    jupyter contrib nbextension install --user &&\
    pytest==5.3.4

# SpaCy and API deps
RUN pip install -U spacy>="3.0.0,<4.0.0" \
    py-processors==3.0.3 \
    fastapi[all]==0.61.1 \
    uvicorn==0.11.8 

# SpaCy trained pipe
RUN python -m spacy download en_core_web_sm
    
# Bundle app source
COPY . .

# Move scripts to local/bin
RUN mv scripts/* /usr/local/bin/ && \
    chmod u+x /usr/local/bin/test-all && \
    rmdir scripts

# Assignment-specific deps
RUN pip install -e ".[all]"

# CMD ["ipython"]
# Launch jupyter
# CMD ["/bin/bash", "/usr/local/bin/launch-notebook.sh"]
# Launch api
# CMD ["uvicorn", "processors_extensions:spacy:api", "--reload", "--port", "8000", "--host", "0.0.0.0"]
CMD ["/bin/bash", "api", "--config", "/app/tests/test-config.yml"]