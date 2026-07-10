def person_info (name,roll_no):
    print("name=",name)
    print("roll no=",roll_no)

person_info("uttara",62) 

def person_keyworod (name,roll_no):
    print("name=",name)
    print("roll no=",roll_no)

person_keyworod(name="xyz",roll_no=10)

  
def person_default (name,roll_no,Class="sy4"):
      print("name=",name)
      print("roll no=",roll_no)
      print("CLASS=",Class) 

person_default("prt",77) 
person_default("uio",8,"sy6")

def person_length(*sub):
     print("sub",sub)


person_length ("python")
person_length("python","c")


