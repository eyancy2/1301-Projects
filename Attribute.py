class Attribute:

  def __init__(self, an, at, ky):
    self.aname = an	# attribute name, e.g., "sno"
    self.atype = at	# attribute type, must be "INTEGER" or "STRING"
    self.key = ky	# boolean. True indicating attribute is KEY, False otherwise

  # getters

  def get_aname(self):
    return self.aname # replace "pass" with code

  def get_atype(self):
    return self.atype

  def get_key(self):
    return self.key

  # setters

  def set_aname(self,an):
    self.aname = an

  def set_atype(self,at):
    self.atype = at

  def set_key(self,ky):
    self.key = ky

  # __str__

  def __str__(self):
    if self.key:
        return self.aname + ":" + self.atype + ":KEY"
    else:
        return self.aname + ":" + self.atype
    
# a1 = Attribute("sno","INTEGER",True)
# a2 = Attribute("sname","INTEGER",False)
# a3 = Attribute("gpa","INTEGER",True)

