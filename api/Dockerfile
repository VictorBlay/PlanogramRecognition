FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Copy local code into docker image, inside the specific folder
ADD ./ /miapi

# Change the work directory to be the specific folder
WORKDIR /miapi

# Install all the modules that the code needs
RUN pip install -r requirements.txt

ENV PORT=8080
# Command that will start the application
CMD uvicorn main:app --host 0.0.0.0 --port=${PORT}