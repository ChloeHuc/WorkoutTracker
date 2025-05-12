'''
TODO
- Create workouts as lists of excercises ✅
- Read workouts from json ✅
- Create excercises using json ✅
- Track stats
- Add sets to excercises ✅
- Noises
- Daily notifications
- Daily tracking
- Max reps attempt excercise ✅
- Create workout tool
- Create workout plan tool
- Data analytics with graphs
- Let you fail excercise
'''

import json
import os
import time as t

ExcerciseClasses={}

class Excercise:
    def __init__(self,name,reps,time,sets,max):
        self.name=name
        self.reps=reps
        self.time=time
        self.sets=sets
        self.max=max

    def display(self):
        if self.max=="True":
            print("Max reps of "+self.name)
            reps=input("How many reps did you do? ")
            print("Done!")
            return
        if self.reps == 0:
            print(self.name + " for " + str(self.time) + " seconds")
            input("Press any key to start")
            t.sleep(self.time)
            print("Done!")
        elif self.time == 0:
            if self.sets!=1:
                print(str(self.sets)+" sets of "+str(self.reps)+" "+str(self.name)+"s")
            else:
                print(str(self.reps)+" x "+str(self.name)+"s")
            input("Press any key to mark finished")
            print("Done!")

def displayWorkout(name):
    file=open("workouts/"+name+".json", "r")
    workoutdata=json.loads(file.read())
    file.close()
    excercises=workoutdata["excercises"]

    for excercise in excercises:
        ExcerciseClasses[excercise+".json"].display()

def loadExcercises():
    for filepath in os.listdir("excercises"):
        file=open("excercises/"+filepath,"r")
        data=json.loads(file.read())
        file.close()
        ExcerciseClasses[filepath]=(Excercise(data["Name"],data["Reps"],data["Time"],data["Sets"],data["Max"]))

loadExcercises()
displayWorkout("newworkout")
quit()
