class Employee:
  def __init__(self, Eid, Ename, Elocation, Esalary):
    self.Eid = Eid
    self.Ename = Ename
    self.Elocation = Elocation
    self.Esalary = Esalary
  def getEmployee(self):
    print("Employee with id " + str(self.Eid) + " and name " + self.Ename + " is from " + self.Elocation + " has a salary of " + str(self.Esalary))
 
