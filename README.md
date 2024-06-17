# Test Project - Containerized Python Api

## How to run:

### Development environment:

#### Create a virtual environment:

```bash
python -m venv venv
```

#### Activate the virtual environment:

```bash
.\venv\Scripts\activate
```

#### Install the dependencies:

```bash
pip install -r requirements.txt
```

#### Run the script:

```bash
python .\src\main.py
```

### Docker environment:

#### Build the image:

```bash
docker build -t test-python-api .
```

#### Run the container:

```bash
docker run -p 5000:5000 test-python-api
```


## Deploye image to Docker Hub:

```bash
docker tag test-python-api nelsonbn/test-python-api:latest
docker push nelsonbn/test-python-api:latest
```
