FROM library/python:3.9

WORKDIR /opt
COPY requirements.txt manage-dependencies/requirements.txt
RUN pip install -r manage-dependencies/requirements.txt

ENTRYPOINT [ "python", "-m", "manage-dependencies" ]
