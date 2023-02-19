
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# UoW student number: w1870614
# Student ID: 20200652       
# Date: 06.12.2021

#create variables
Pass=0
Defer=0
Fail=0
#Creating a list for credits.
list = []
Credit_List=[]

def Progress(Pass,Defer,Fail):
    if (Pass==120):
        return("Progress")
    elif (Pass==100 and (Defer==20 or Fail==20)):
        return("Progress (module trailer)")
    elif(Fail<80):
        return("Module retriever ")
    elif(Fail>=80):
        return("Excluded")
def get():
    valid=[0,20,40,60,80,100,120]
    while True:
        try:
            Pass=int(input("Enter your Pass credits :"))
            if Pass not in valid:
                print("Out of range.\n")
                continue
            Defer=int(input("Enter your Defer credits :"))
            if Defer not in valid:
                print("Out of range.\n")
                continue
            Fail=int(input("Enter your Fail credits :"))
            if Fail not in valid:
                 print("Out of range.\n")
                 continue
        except:
            print("Integer required.\n")
            continue
        else:
            if(Pass+Defer++Fail)!=120:
                print("Total incorrect.\n)")
                continue
            else:
                return Pass,Defer,Fail
            
print("-"*20 )
print("Staff Version with Histogram ")
print("\n")
progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0
run = True
while run:
    Pass, Defer, Fail = get()
    Value = Progress(Pass, Defer, Fail)
    if Value == "Progress":
        Credit_List = [f'Progress -{Pass},{Defer},{Fail}']
        list.append(Credit_List)
        progress_count += 1
    elif Value == "Progress (module trailer)":
        Credit_List = [f'Progress (module trailer) -{Pass},{Defer},{Fail}']
        list.append(Credit_List)
        trailer_count += 1
    elif Value == "Excluded":
        Credit_List =[f'Exclude -{Pass},{Defer},{Fail}']
        list.append(Credit_List)
        excluded_count += 1
    else:
        Credit_List = [f'module retriever -{Pass},{Defer},{Fail}']
        list.append(Credit_List)
        retriever_count += 1
    print(Value + "\n")
    user = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    print("\n")
    if user.lower() == 'q':
        run = False
#for d in list:
#    for k in d:
#        print(k,end='')
#    print()
    
