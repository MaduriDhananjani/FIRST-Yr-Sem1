# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# UoW student number: w1870614
# Student ID: 20200652       
# Date: 29.11.2021
#create variables
Pass=0
Defer=0
Fail=0

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
            Pass=int(input("Enter your Pass credits :"))#asking credits
            if Pass not in valid:
                print("Out of range.\n")
                continue
            Defer=int(input("Enter your Defer credits :"))#asking credits
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
                print("Total incorrect.\n)")
                continue
            else:
                return Pass,Defer,Fail
print("-----------------------------------------------------------" )
print("Staff Version with Histogram ")
print("\n")
#creat variables

progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0
run = True
while run:
    Pass, Defer, Fail = get()
    Value = Progress(Pass, Defer, Fail)
    if Value == "Progress":
        progress_count += 1
    elif Value == "Progress (module trailer)":
        trailer_count += 1
    elif Value == "Excluded":
        excluded_count += 1
    else:
        retriever_count += 1
    print(Value + "\n")
    user = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    print("\n")
    if user.lower() == 'q':
        run = False


print("----------------------------------------------------------")
#part 2
#vertical Histogram
print("Vertical Histrogram")
print("     progress ", "Trailer ", "Retriever ", "Exclude")
for i in range(max(progress_count, trailer_count, retriever_count, excluded_count)):

    if (i < progress_count):
        print("\t*", end=' ')
    else:
        print("\t ", end=' ')

    if (i < trailer_count):
        print("\t  *", end=' ')
    else:
        print("\t ", end=' ')

    if (i < retriever_count):
        print("\t   *", end=' ')
    else:
        print("\t ", end=' ')

    if (i < excluded_count):
        print("\t       *", end=' ')
    else:
        print("\t ", end=' ')
    print()
 
           
