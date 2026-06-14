# Task Manager CLI
A command-line task management application built with Python.
 Where users can create projects, assign tasks, track task status,
 and manage users through a simple CLI Interface
## Features
- Create and manage users
- Create and manage projects
- Create tasks and assign them to users
- Mark tasks as complete
- Command-line interface using argparse
- Object-oriented design with inheritance
- Encapsulation and object(class) relationships
## Technologies used 
- Python 3.14
- argparse
- object-oriented programming(OOP)
## Installation
Clone the repository
  ```bash
git clone https://github.com/munirasheikh-rgb/summative2-Python-CLI.git
 ```
Navigate to the project folder
  ```bash
 cd summative2-Python-CLI
  ```
 install dependencies
 ```bash
pip install -r requirements.txt
 ```
## Usage
Create a user
```bash
 python3 main.py add-user "user" "user@email.com"
```
Create a project
 ```bash
python3 main.py add-project "CLI tools"
  ```
Add a task
  ```bash
python3 main.py add-task "build project management with CLI"
 ```
Mark tasks as complete
  ```bash
python3 main.py complete-task 1
  ```
## Object-oriented concepts demonstrated
- Inheritance (Person --> User)
- Encapsulation (properties and setters)
- Relationship between objects

## How to run tests
```bash
 python3 -m pytest
  ```
## Author👩‍💻 
Munira Hassan
