# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# UoW student number: w1870614
# Student ID: 20200652       
# Date: 25.11.2021

#1.
#Creat Variables
Pass=0
Defer=0
Fail=0

#Input

Pass=int(input("Enter your pass credidts:"))
Defer=int(input("Enter your Defer credidts:"))
Fail=int(input("Enter your Fail credidts:"))

#Process & Output

def process (Pass,Defer,Fail):
    
    if(Pass==120):
        print("Progress")
    elif(Pass==100 and (Defer==20 or Fail==20)):
        print("Progress (module trailer)")
    elif(Fail<80):
        print("Do not progress-module retiever")
    elif(Fail>=80):
        print("Exclude")

process(Pass,Defer,Fail)        

