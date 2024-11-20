class Relation:

  def __init__(self, rname, attrs):
    self.rname = rname
    self.attributes = attrs

  # return string representation of relation
  # see sample run for formatting
  def __str__(self):
    return self.rname + "(" + str(self.attributes) + ")"
    
  


