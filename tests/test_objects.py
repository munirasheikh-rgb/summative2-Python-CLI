import pytest
from models.objects import User,Project,Task

def test_user_add_user_to_collection():
    User.users = []
    User.next_id = 1

    user = User.create_user("Munira", "munira@hassan.com")
    assert user.name == "Munira"
    assert user.email == "munira@hassan.com"
    assert user .id == 1
    assert user in User.users

def test_user_can_add_project():
    user  = User.create_user("Maryam" , "maryam@05.com")
    project = Project("CLI tool", "biuld project manager", "2026-06-12") 

    user.add_projects(project)
    assert project in user.projects
    assert user.projects[0].title =="CLI tool"

def test_task_can_be_assigned_to_user_and_mark_compete() :
    user = User("Hiba", "hiba@hassan.com")
    task = Task("create CLI subcommands", "pending") 

    task.assign_user(user)  
    task.mark_task_as_complete()

    assert task.assigned_to == user
    assert task in user.tasks
    assert task.status == "completed"