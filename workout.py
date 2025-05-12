'''
TODO
- Create workouts as lists of excercises
- Read workouts from json ✅
- Track stats
- Add sets to excercises
- Noises
- Daily notifications
- Daily tracking
- Max reps attempt excercise
- Create workout tool
- Create workout plan tool
- Data analytics with graphs
- Let you fail excercise
'''

import json
import time as t

class Excercise:
    def __init__(self,name,reps,time):
        self.name=name
        self.reps=reps
        self.time=time

    def display(self):
        if self.reps == 0:
            print(self.name + " for " + str(self.time) + " seconds")
            input("Press any key to start")
            t.sleep(self.time)
            print("Done!")
        elif self.time == 0:
            print(str(self.reps)+" x "+str(self.name)+"s")
            input("Press any key to mark finished")
            print("Done!")

def displayWorkout(name):
    file=open("workouts/"+name+".json", "r")
    workoutdata=json.loads(file.read())
    file.close()
    excercises=workoutdata["excercises"]

    for excercise in excercises:
        globals()[excercise].display()


ShortHang=Excercise("Hang",0,5)
LowPullups=Excercise("Pullups",3,0)
displayWorkout("newworkout")
quit()
