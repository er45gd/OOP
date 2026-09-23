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

def add():
    name=input("Enter student name:")
    scoreOne=int(input("Enter score one:"))
    scoreTwo=int(input("Enter score two:"))
    scoreThree=int(input("Enter score three:"))
    scoreFour=int(input("Enter score four:"))
    scoreFive=int(input("Enter score five:"))
    addTotal=scoreOne+scoreTwo+scoreThree+scoreFour+scoreFive
    addPercentage= addTotal/100
    addAverage=addTotal/5
    studentLabScore.update()

    print ("studentLabScore")

def delete():
    tbd=input(print("which student number do you want to remove?: "))
    h="Student"+tbd
    del studentLabScore[h]

    print(studentLabScore)