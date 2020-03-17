import datetime
import string
import time as tm
class Tech_mentor_and_learner:
    def addStacks(self,x):
        interest.append(x)
        #print(interest)
    def setMentorOrLearner(self,x):
        if(x.lower()=="mentor"):
            self.setAvailableTime()
    def setAvailableTime(self):
        time=input("Enter available time in hh:mm:ss format: ")
        mentor.append([interest[-1],time])
        #print(mentor)
    def getMentor(self):
        stack=input("Enter your area of interest: ")
        time=input("Enter time in (hh:mm:ss) format: ")
        hh_mm_ss=time.split(":")
        cur=datetime.time(int(hh_mm_ss[0]),int(hh_mm_ss[1]),int(hh_mm_ss[2]))
        counter=0
        for key in mentor:
            if (key[0] == stack):
                men_list=key[1].split(":")
                men_time=datetime.time(int(men_list[0]),int(men_list[1]),int(men_list[2]))
                if(cur==men_time):
                    counter=counter+1
        print("Checking for mentor availability......\n")
        tm.sleep(1)
        print(counter," mentor(s) are currently available")
        

if __name__=="__main__":
    flag=True
    interest=[]
    mentor=[]
    ls=[]
    while(flag==True):
        print("\nOptions:\n1. Add an area of interest/expertise\n2. Set whether mentor or learner\n3. Check mentor availability\n4. Exit")
        option=int(input("Enter your choice: "))
        t=Tech_mentor_and_learner()
        if(option==1):
            x=input("Enter an area of Interest/Expertise: ")
            t.addStacks(x)
        elif(option==2):
            x=input("Enter whether you're a mentor or learner: ")
            t.setMentorOrLearner(x)
        elif(option==3):
            t.getMentor()
        else:
            flag=False
              
