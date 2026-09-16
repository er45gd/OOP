myDiction={"name1":"Ethan","name2":"Trevor","name3":"Grant",}#"name4":"Kade","name5":"Aubree","Name6":"Megan"}

print(myDiction)

myDiction.update({"name4":"Kade"})
print(myDiction)
myDiction.update({"name5":"Aubree"})
print(myDiction)
myDiction.update({"name6":"Megan"})
print(myDiction)

#off to college
del myDiction[("name1")]
print(myDiction)

myDiction["name5"]= "Bree"
print(myDiction)