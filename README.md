### Set up & Activate the virtual environment ###

Set up & Activate the virtual environment
```
python -m venv venv  #on Linux use python3 -m venv venv
```

```
cd venv\Scripts
activate.bat
python ..\..\app.py
```

### Install dependencies ###

```
pip3 install -r requirements.txt
```
### Concepton ###

![alt text](image-1.png)


### Architeture d'implementation ###

![alt text](image.png)

### Tests ###

POST http://localhost:3000/todos

![img.png](img.png)

GET http://localhost:3000/todos
![img_1.png](img_1.png)