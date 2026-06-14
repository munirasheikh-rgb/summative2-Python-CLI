import json 
DATA_FILE = "data/data.json"

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data,file,indent=3)

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
         return json.load(file)     
    except FileNotFoundError:
       return{"users":[],
              "projects":[],
               }
           