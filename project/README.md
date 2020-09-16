## Step 1 : Create python virtual environment by "virtualenv" or "pipenv"
## Step 2 : Install Redis Server, create a database "my_db", and review "REDIS_URL" configuration in file "shop/__init__.py"
## Step 3 : Restart the virtual machine from "Step 1", and run "pip install -r requirements.txt" in folder /project
## Step 4 : Run command line "python run.py" in folder /project to restart flask server and run http://localhost:5000
## Step 5 : Open the Postman to test the task "Catalog" with "GET, POST, PUT, DELETE":
    - POST, GET LIST: http://localhost:5000/products
    - GET: http://localhost:5000/product/<uuid>