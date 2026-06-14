import json 
DATA_FILE = "data/data.json"
# saves project data to the json file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data,file,indent=3)
        
#loads project data from json file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
         return json.load(file)     
    except FileNotFoundError:
       return{"users":[],
              "projects":[],
               }
           