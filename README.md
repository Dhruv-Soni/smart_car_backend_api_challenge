# smart_car_backend_api_challenge
smart car backend api challenge 

## git clone this project

## download python3 and the latest pip
```
https://realpython.com/installing-python/
```

## cd into this directory
```
./smart_car_backend_api_challenge/
```

## install venv
```
On macOS and Linux:
python3 -m pip install --user virtualenv

On Windows:
py -m pip install --user virtualenv
```

### Create a virtual environment
```
On macOS and Linux:
python3 -m venv env

On Windows:
py -m venv env
```

### Activate venv
```
On macOS and Linux:
source env/bin/activate

On Windows:
.\env\Scripts\activate
```

### install requirements
```
pip install -r requirements.txt
```

### start flask server
```
flask run
```

it will be running on http://127.0.0.1:5000/. if an error occurs saying that it is already in use, this will help: https://stackoverflow.com/questions/34457981/trying-to-run-flask-app-gives-address-already-in-use

### Running the testcases
```
python test_apis.py -v 
```
-v option is for verbose
