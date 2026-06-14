class Person:
   def __init__(self,name,email):
      self.name = name
      self.email = email

class User(Person):
    users = []
    next_id = 1
    def __init__(self,name,email):
      super().__init__(name,email)
      self.id = User.next_id
      User.next_id += 1
      self.projects = []
      self.tasks = []

    @classmethod
    def create_user(cls,name,email):
       user = cls(name,email)
       cls.users.append(user)
       return user
    
    @classmethod
    def list_user(cls):
       return cls.users
    
    @property
    def name(self):
       return self._name
    @name.setter
    def name(self,value):
       if value == "":
          raise ValueError("Name cannot be empty")
       self._name = value
       
    
    def __str__(self):
      return f"{self.name}: {self.email}"
    
    def add_projects(self,project):
       self.projects.append(project)


    def list_projects(self):
       for project in self.projects:
          print(project.title)



class Project:
   projects = []
   next_id = 1
   def __init__(self,title,description,due_date):
      self.title = title 
      self.description = description
      self.due_date = due_date
      self.id =Project.next_id
      Project.next_id +=1
      self.tasks = []

      Project.projects.append(self)
    
   def __str__(self):
      return f"{self.title}"


   def add_task(self,task):
      self.tasks.append(task)

   def list_task(self):
      for task in self.tasks:
         print(task.title)

class Task:
   tasks = []
   next_id = 1
   def __init__(self,title,status):
      self.title = title
      self.status = status
      self.id = Task.next_id
      Task.next_id += 1
      
      self.assigned_to = None

   def __str__(self):
      return f"{self.title} ({self.status})"
   @property
   def status(self) :
      return self._status
   @status.setter
   def status(self,value):
      if value == "":
         raise ValueError("fill in the status")
      self._status = value
        

   def mark_task_as_complete(self):  
      self.status = "completed"
      print(f"Task {self.title} marked as complete")

   def assign_user(self,user):
      self.assigned_to = user
      if self not in user.tasks:
        user.tasks.append(self)

if __name__ == "__main__"  :      

   u1 = User.create_user("Munira","'munira@hassan.com")
   u2 = User.create_user("Maryam","maryam@05.com")
   print(u1.id)
   print(u1.name)
   print(User.list_user())

   p1 = Project("Python CLI tool","project management tool","2026-06-12")
   u1.add_projects(p1)
   print(u1.projects[0].title)

   t1 = Task("create project commands","complete")
   p1.add_task(t1)
   print(p1.tasks[0].title)

   t1.assign_user(u1)
   print(t1.assigned_to.name)
   print(u1.tasks[0].title)
         
   t1.mark_task_as_complete()
   print(t1.status)
   