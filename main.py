import argparse
from utils.utils import load_data,save_data
from models.objects import User,Project,Task
def create_user(args):
    try:
        user= User.create_user(args.name,args.email)
        print(user)
    except ValueError as error:
        print(f"Error: {error}")  



def add_projects(args):
   data = load_data()
   project ={
       "id":len(data["projects"]) +1,
       "user":args.user,
       "title":args.title,
       "description":args.description,
       "due_date":args.due_date,
       "tasks":[]
   }
   data["projects"].append(project)
   save_data(data)
   #print(type(data))
   print(f"project added:{args.title} to {args.user}")

def add_task(args):
    data = load_data()
    task = {"title":args.title,
            "status":args.status}
    
    for project in data["projects"]:
        if project["id"] == int(args.project_id):
            project["tasks"].append(task)
            save_data(data)
            print(f"Task added:{args.title} to project {project["title"]}")
            return
        
    print("Project not found")
        

def mark_task_as_complete(args):
        for task in Task.tasks:
            if task.title == args.title:
                task.mark_task_as_complete()
                print("Task completed")
        else:
          print("Task not found")            

parser = argparse.ArgumentParser(description= "Project Management CLI")
subparsers = parser.add_subparsers(required=True)

create_parser = subparsers.add_parser("create-user", help="create a user")
create_parser.add_argument("name")
create_parser.add_argument("email")
create_parser.set_defaults(func=create_user)


add_project_parser = subparsers.add_parser("add-project", help="Add project to a user")
add_project_parser.add_argument("user")
add_project_parser.add_argument("title")
add_project_parser.add_argument("description")
add_project_parser.add_argument("due_date")
add_project_parser.set_defaults(func=add_projects)

addt_task_parser = subparsers.add_parser("add-task", help="Add task to a project")
addt_task_parser.add_argument("project_id")
addt_task_parser.add_argument("title")
addt_task_parser.add_argument("status")
addt_task_parser.set_defaults(func=add_task)


mark_parser = subparsers.add_parser("mark-complete", help="Mark a task complete")
mark_parser.add_argument("title")
mark_parser.set_defaults(func=mark_task_as_complete)





args = parser.parse_args()
args.func(args)

