from Attributes import *
from Relation import *

class Relations:

  def __init__(self):
    self.relations = {}

  # insert relation object r into dictionary
  # return True if success, False otherwise
  def insert(self,r):
    if r.rname in self.relations:
        return False  # Relation already exists
    self.relations[r.rname] = r
    return True

  # delete relation with name rname from dictionary
  # return relation object for name if success, None otherwise
  def delete(self,rname):
    # return self.relations.pop(rname, None)
    if rname in self.relations:
      r = self.relations[rname]
      del self.relations[rname]
      return r 
    return None 

  # return relation object for relation with name rname
  # return None if not found
  def get_relation(self,rname):
    return self.relations.get(rname, None)

  # return string representation of all relation objects
  # see sample run for formatting
  def __str__(self):
    return "\n".join(str(rel) for rel in self.relations.values())
    
  
  
