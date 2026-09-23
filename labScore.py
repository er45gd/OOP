studentLabScore={}
 #   "student1":{
  #      "name":"",
   #     "lab1":"",
    #    "lab2":"",
    #    "lab3":"",
     #   "lab4":"",
      #  "lab5":"",
      #  "total":"",
       # "percent":"",
        #"average":"
 #   }
#}
i=1
def add():
    name=input("Enter student name:")
    scoreOne=int(input("Enter score one:"))
    scoreTwo=int(input("Enter score two:"))
    scoreThree=int(input("Enter score three:"))
    scoreFour=int(input("Enter score four:"))
    scoreFive=int(input("Enter score five:"))
    total=scoreOne+scoreTwo+scoreThree+scoreFour+scoreFive
    percentage= total/100
    average=total/5
    studentNumber="student"+str(i)
    studentLabScore.update({studentNumber:
        {
            "name":name,
            "scoreOne":scoreOne,
            "scoreTwo":scoreTwo,
            "scoreThree":scoreThree,
            "scoreFour":scoreFour,
            "scoreFive":scoreFive,
            "total":total,
            "average":average,
            "percentage":percentage

        }})

    print(studentLabScore)

def delete():
    tbd=input(print("which student number do you want to remove?: "))
    h="Student"+str(tbd)
    del studentLabScore[h]

    print(studentLabScore)


add()
