import argparse
from utils.utils import load_data,save_data
from tabulate import tabulate
#from models.objects import User,Project,Task

#creates a new user and saves to data.json
def create_user(args):
    data = load_data()
    user = {"name": args.name,
            "email":args.email} 
    data["users"].append(user)
    save_data(data) 
    print(f"User {args.name} created")


#Adds a new project to a user
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

#add a task to a project using project id
def add_task(args):
    data = load_data()
    task = {"title":args.title,
            "status":args.status}
    
    for project in data["projects"]:
        if project["id"] ==(args.project_id):
            project["tasks"].append(task)
            save_data(data)
            print(f"Task added:{args.title} to project {project["title"]}")
            return
        
    print("Project not found")
        
#marks task as complete using its title
def mark_task_as_complete(args):
        data = load_data()
        for project in data["projects"]:
            for task in project["tasks"]:
                if task["title"] == args.title:
                    task["status"] ="completed"
                    save_data(data)
                print(f"Task '{args.title}' marked as complete")
                return
        print("Task not found") 

#assign a task to a user
def assign_user(args):
    data = load_data()
    for project in data["projects"]:
        for task in project["tasks"]:
            if task["title"] == args.title:
                task["assigned_to"] =args.user
                save_data(data)
                print(f"Task {args.title} assigned to {args.user}")
                return
    print("Task not found")  

#displays all projects in table format
def list_projects(args):
    data = load_data()
    table = []
    for project in data["projects"]:
        table.append([project["id"],project["title"],project["user"],project["due_date"]])
    print(tabulate(table,headers=["ID","Title","User","Due_date"]))
    
#displays all tasks inside a project
def list_tasks(args):
    data = load_data() 
    for project in data["projects"]:
     print(f"Project:{project["title"]}")
     for task in project["tasks"]:
        print(f"{task["title"]} - {task["status"]}")
#search projects assigned to a specific user
def search_user_projects(args):
    data = load_data()   
    for project in data["projects"]:
        if project["user"] == args.user:
          print(f"{project["id"]} - {project["title"]}")      


                            

      

parser = argparse.ArgumentParser(description= "Project Management CLI")
subparsers = parser.add_subparsers(required=True)

create_parser = subparsers.add_parser("create-user", help="create a user")
create_parser.add_argument("name")
create_parser.add_argument("-e","--email")
create_parser.set_defaults(func=create_user)


add_project_parser = subparsers.add_parser("add-project", help="Add project to a user")
add_project_parser.add_argument("-u","--user")
add_project_parser.add_argument("title")
add_project_parser.add_argument("description")
add_project_parser.add_argument("-d","--due_date")
add_project_parser.set_defaults(func=add_projects)

addt_task_parser = subparsers.add_parser("add-task", help="Add task to a project")
addt_task_parser.add_argument("project_id", type=int)
addt_task_parser.add_argument("title")
addt_task_parser.add_argument("--status")
addt_task_parser.set_defaults(func=add_task)


mark_parser = subparsers.add_parser("mark-complete", help="Mark a task complete")
mark_parser.add_argument("title")
mark_parser.set_defaults(func=mark_task_as_complete)


assign_parser = subparsers.add_parser("assign-user", help="Assign a user to a task")
assign_parser.add_argument("title")
assign_parser.add_argument("-u","--user")
assign_parser.set_defaults(func=assign_user)

list_projects_parser = subparsers.add_parser("list-projects" ,help="List all projects")
list_projects_parser.set_defaults(func=list_projects)

list_task_parser = subparsers.add_parser("list-task" ,help="List all tasks")
list_task_parser.set_defaults(func=list_tasks)


search_projects_parser = subparsers.add_parser("user-projects",help="list all projects assigned to a user")
search_projects_parser.add_argument("--user")
search_projects_parser.set_defaults(func=search_user_projects)
if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)

