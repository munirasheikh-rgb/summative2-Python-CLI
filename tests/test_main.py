from utils.utils import load_data
from main import create_user, add_projects
from models.objects import User

def test_load_data_returns_dictionary():
    data = load_data()
    assert isinstance(data,dict)

def test_data_contains_projects():
  data = load_data()
  assert "projects" in data

def test_user_creation():
   user = User("Munira" , "munira@hassan.com")
   assert user.name == "Munira"  

class Args:
   pass

def test_create_user_adds_user():
   args = Args()
   args.name = "Munira"
   args.email = "munira@hassan.com"

   create_user(args)
   data =load_data()
   assert {"name":"Munira","email":"munira@hassan.com"} in data["users"]

def test_add_project_adds_project():
      args = Args()
      args.user = "Munira"
      args.title = "CLI tools"
      args.description = "build CLI project app"
      args.due_date= "2026-06-12"

      add_projects(args)
      data = load_data()
      assert any(project["title"] == "CLI tools" for project in data["projects"])
    