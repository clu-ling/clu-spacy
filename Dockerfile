FROM python:3.8

LABEL author="Zachary Wellington"
LABEL description="Image definition for Python-based SpaCy Doc/CluDocument converter."

# Set up and activate virtual environment
#   Reccomended by SpaCy
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Create app directory
WORKDIR /app

# Bundle app source
COPY . .

# Move scripts to local/bin
RUN mv scripts/* /usr/local/bin/
RUN rmdir scripts

# Install python dependencies
RUN pip install -U pip

# SpaCy and pre-trained pipeline
RUN pip install -U pip setuptools wheel
RUN pip install requirements.txt

# iPython
RUN pip install -U ipython==7.19.0

# Jupyter deps
RUN pip install -U jupyter==1.0.0
RUN pip install -U jupyter-contrib-nbextensions==0.5.1
RUN jupyter contrib nbextension install --user

# Assignment-specific deps
RUN pip install -e ".[all]"
#CMD ["ipython"]
# Launch jupyter
CMD ["/bin/bash", "/usr/local/bin/launch-notebook.sh"]