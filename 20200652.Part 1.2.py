# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# UoW student number: w1870614
# Student ID: 20200652       
# Date: 29.11.2021

#2.validations
#creat Variebles
Pass=0
Defer=0
Fail=0

def Progress (Pass,Defer,Fail):
    if (Pass==120):
        return ("Progress")
    elif (Pass==100 and ( Defer==20 or Fail ==20)):
        return("Progress (module trailer")
    elif( Fail<80):
        return("Do not progress-module retriever")
    elif( Fail>=80):
        return("Exclude")
def get():
    valid=[0,20,40,60,80,100,120]
    while True:
        try:
            Pass=int(input("Enter your Pass credits :")) #asking credits
            if Pass not in valid:
                print("Out of range.\n")
                continue
            Defer=int(input("Enter your Defer credits :"))#asking credidt
            if Defer not in valid:
                print("Out of range.\n")
                continue
            Fail=int(input("Enter your Fail credits :"))#asking credits
            if Fail not in valid:
                 print("Out of range.\n")
                 continue
        except:
            print("Integer required.\n")
            continue
        else:
            if(Pass+Defer++Fail)!=120:
                print("Total incorrect.\n")
                continue
            else:
                
                return Pass,Defer,Fail
#get permission
Pass,Defer,Fail=get()

print(Progress(Pass,Defer,Fail))
print("----------------------------------------------------")


