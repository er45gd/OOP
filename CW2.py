#new blank list
THElist = []

#adds 5 values to list
for i in range(1, 6):
    print("add the value #",i)
    THElist.append(int(input()))
    print(THElist)
#removes chosen value
print("which on should i remove")
r=int(input())
for i in THElist:
    THElist.remove(r)
    print(THElist)
    break
else:
    print("that doesn't exist silly")

#asks for value to replace
print("which one to replace")
old_element=int(input())
print("whats the new value")
newNumber=int(input())
#does the replacing
index = THElist.index(old_element)
THElist[index]=newNumber
print(THElist)

#formatting/sorting
print("")
print("sorting the list from highest to lowest")
THElist.sort()
print(THElist)

exit() #done