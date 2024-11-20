import sys
from Relations import *
from Attributes import *

# load_schema()
# student,sno:i:y,sname:s:n,phone:s:n
def load_schema(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    relations = Relations()
    for d in data:
        xs = d.split(",")
        rname = xs[0]
        attrs = xs[1:]
        attrs_obj = Attributes()
        for pos,attr in enumerate(attrs):
            aname,atype,key = attr.split(":")
            key = True if key=='y' else False
            #key (key=='y')
            atype = "STRING" if atype=='s' else "INTEGER"
            a = Attribute(aname,atype,key)
            attrs_obj.insert(a,pos+1)
        r = Relation(rname,attrs_obj)
        relations.insert(r)
    return relations

# write data from relations data structure to file fname
def store_schema(fname,relations):
  with open(fname,"w") as f:
    num_relations = len(relations.relations)
    count = 0
    for rname in relations.relations:
      count = count + 1
      f.write(rname)
      f.write(",")
      attrs = relations.relations[rname].attributes.attributes
      for index,a in enumerate(attrs):
        f.write(a.aname)
        if a.atype == "INTEGER":
          f.write(":i:")
        else:
          f.write(":s:")
        if a.key:
          f.write("y")
        else:
          f.write("n")
        if index != len(attrs)-1:
          f.write(",")
      if count != num_relations:
        f.write("\n")
  f.close()
    
def menu():
  print("\ni. DEFINE RELATION SCHEME")
  print("m. MODIFY RELATION SCHEME")
  print("d. DELETE RELATION SCHEME")
  print("p. PRINT DATABASE SCHEME")
  print("q. QUIT\n")

def define_relation(rname,relations):
  inn = input("Attributes: aname1:atype1:key1,aname2:atype2:key2:etc:\n")
  ats = inn.split(",")
  attrs = Attributes()
  for i,attr in enumerate(ats):
    aname,atype,key = attr.split(":")
    key = True if key == 'y' else False
    atype = 'INTEGER' if atype=='i' else 'STRING'
    attr = Attribute(aname,atype,key)
    attrs.insert(attr,i+1)
  r = Relation(rname,attrs)
  if relations.insert(r):
    print("Relation",rname,"inserted")
  else:
    print("Relation",rname,"cannot be inserted.")

def modify_relation(rname,relations):
  rel = relations.get_relation(rname)
  if rel is not None:
    cmd = input("a aname:atype:key:pos, d aname: ").split()
    if cmd[0] == 'a' or cmd[0] == 'A':
      aname,atype,key,pos = cmd[1].split(":")
      key = True if key == 'y' else False
      atype = 'INTEGER' if atype=='i' else 'STRING'
      pos = int(pos)
      if pos <= 0 or pos > 1+rel.attributes.size():
        print("Invalid position",pos)
        return
      attr = Attribute(aname,atype,key)
      if rel.attributes.insert(attr,pos):
        print("Attribute",str(attr),"inserted!")
      else:
        print("Could not insert attribute")
        return
    elif cmd[0] == 'd' or cmd[0] == 'D':
      aname = cmd[1].strip()
      if rel.attributes.delete(aname):
        print("Attribute",aname,"deleted!")
      else:
        print("Attribute",aname,"NOT deleted!")
        return
    else:
      print('Invalid option')
    r = Relation(rname,rel.attributes)
  else:
    print("Relation %s does not exist"%rname)

def main():
  relations = load_schema(sys.argv[1])
  while True:
    menu()
    cmd = input("Enter your option (i rname, d rname, m rname, p, q): ").strip().lower()
    if cmd[0] == 'i':
      rname = cmd[1:].strip()
      if relations.get_relation(rname) is None:
        define_relation(rname,relations)
      else:
        print("Relation with name",rname,"already exists")
    elif cmd[0] == 'm':
      rname = cmd[1:].strip()
      if relations.get_relation(rname) is not None:
        modify_relation(rname,relations)
      else:
        print("Relation with name",rname,"does not exist")
    elif cmd[0] == 'd':
      rname = cmd[1:].strip()
      if relations.delete(rname):
        print("Relation %s has been deleted"%rname)
      else:
        print("Relation %s does not exist"%rname)
    elif cmd[0] == 'p':
      print()
      print(relations)
    elif cmd[0] == 'q':
      break
    else:
      print("Invalid option\n")
  store_schema(sys.argv[1],relations)

main()