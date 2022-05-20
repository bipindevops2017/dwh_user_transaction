#Deriving the latest base image
FROM python:latest

# Any working directory /usr/app/src
WORKDIR /usr/app/src

# Installing Required libraries
RUN pip install pandas

# COPY the python file at working directory in container
COPY Solution.py ./
# Now the structure looks like this '/usr/app/src/test.py'

#running Pyhton file in container
CMD [ "python", "./Solution.py", ">","./output.py"]