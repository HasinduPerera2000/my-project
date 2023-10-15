class Person:
    def __init__(self, name, id, email, age):
        self.name = name
        self.id = id
        self.email = email
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Email: {self.email}, Age: {self.age}"    
