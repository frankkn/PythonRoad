class Student:
  def __init__(self, name, ID): # constructor
    self.name = name
    self.ID = ID
  def showMe(self):
    print('Name:', self.name, 'ID:', self.ID)
  def changeName(self, newName):
    self.name = newName

a = Student('David', 12345)
print(a.showMe())
a.changeName('Frank')
print(a.showMe())
b = Student('Amy', '67890')