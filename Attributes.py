from Attribute import *

class Attributes:

  def __init__(self):
    self.attributes = []

  # insert attribute a in position pos
  # return True if success, False otherwise
  def insert(self,a,pos):
    if pos <= 0 or pos > len(self.attributes)+1:
      return False
    self.attributes.insert(pos-1,a)
    # self.attributes = self.attributes[0:pos] + [a] + self.attributes[pos-1:]
 
  # delete attribute with name aname
  # return True if success, False otherwise
  def delete(self,aname):
    for i, attr in enumerate(self.attributes):
            if attr.get_aname() == aname:
                del self.attributes[i]
                return True
    return False
    

  # return True if attribute with name aname is present
  # return False otherwise
  def member(self,aname):
    # return any(attr.get_aname() == aname for attr in self.attributes)
    for attr in self.attributes:
       if attr.get_aname() == aname:
          return True
    return False

  # return number of attributes
  def size(self):
    return len(self.attributes)

  # return string to print attributes.
  # see sample run of program for exact formatting
  def __str__(self):
    return ", ".join(str(attr) for attr in self.attributes)
    
  
