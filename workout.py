'''
TODO
- Create workouts as lists of excercises
- Read workouts from json
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


def displayExcercise(name,number,time):
    if number == 0:
        print(name + " for " + str(time) + " seconds")
        input("Press any key to start")
        t.sleep(time)
        print("Done!")
    elif time == 0:
        print(str(number)+" x "+str(name)+"s")
        input("Press any key to mark finished")
        print("Done!")

#def startWorkout()

ShortHang=Excercise("Hang",0,5)
LowPullups=Excercise("Pullups",3,0)
ShortHang.display()
LowPullups.display()
quit()
