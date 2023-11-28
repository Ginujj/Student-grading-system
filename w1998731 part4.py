# I declear that this is my own work and i did not include any other
# person's work in this project. 

#___________________________________ Defining lists

credit_range = [0, 20, 40, 60, 80, 100, 120]

progress_list            = [120,0,0]
module_trailer_list      = [[100,20,0],[100,0,20]]
module_retriever_list    = [[80,40,0],[80,20,20],[80,0,40],[60,60,0],[60,40,20],[60,20,40],[60,0,60],[40,80,0],[40,60,20],[40,40,40],[40,20,60],[20,100,0],[20,80,20],[20,60,40],[20,40,60],[0,120,0],[0,100,20],[0,80,40],[0,60,60]]
exclude_list             = [[40,0,80],[20,20,80],[20,0,100],[0,40,80],[0,20,100],[0,0,120]]

#___________________________________ Input_lists

progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
exclude_count = 0

all_result = {}

#___________________________________ Defining functions

def student_or_staff_func():
    global student_or_staff
    while True:
        print()
        student_or_staff = input("Please enter '0' for student , enter '1' for staff member or enter 'q' to quit : ")
        print()
        if student_or_staff == "0" or student_or_staff == "1" or  student_or_staff == "q" :
            break
        else:
            print("Invalid response")
            continue
    
    

    
def credit_input_func():

    global student_outcome
    global progress_count
    global module_trailer_count
    global module_retriever_count
    global exclude_count

    student_id = input("Please enter your ID : ")
    print()
    
    while student_or_staff == "0" or student_or_staff == "1" or student_or_staff == "q":
        pass_credits = input("Enter pass credits value  : ")
        try:
            pass_credits = int(pass_credits)
        except ValueError:
            print("Integer required")
            continue
        if pass_credits not in credit_range:
            print("Out of range")
            continue
        else:
            break

    while True:
        defer_credits = input("Enter defer credits value : ")
        try:
            defer_credits = int(defer_credits)
        except ValueError:
            print("Integer required")
            
            continue
        if defer_credits not in credit_range:
            print("Out of range")
            continue
        else:
            break

    while True:
        fail_credits = input("Enter fail credits value  : ")
        try:
            fail_credits = int(fail_credits)
        except ValueError:
            print("Integer required")
            continue
        if fail_credits not in credit_range:
            print("Out of range")
            continue
        else:
            break

    total_credits = pass_credits + defer_credits + fail_credits

    

    result_list = [pass_credits,defer_credits,fail_credits]
    

    
    if total_credits != 120 :
            print("Total incorrect")
            print("___________________________________")
            print()
            credit_input_func()
            
    elif result_list == progress_list:
        print("___________________________________ Progress")
        student_outcome = "progress"
        progress_count += 1 
                
    elif result_list in module_trailer_list:
        print("___________________________________ Progress (Module trailer)")
        student_outcome = "Module trailer"
        module_trailer_count += 1
    
    elif result_list in exclude_list:
        print("___________________________________ Exclude")
        student_outcome = "Exclude"
        exclude_count += 1
    
    elif result_list in module_retriever_list:
        print("___________________________________ Do not progress - module retriever")
        student_outcome = "module retriever"
        module_retriever_count += 1

    else:
        print("Something went wrong")

    result_list_str = student_outcome + " - " + str(result_list)[1:-1]      
    all_result.update({student_id : result_list_str })




#___________________________________ Ask whether student or a staff


student_or_staff_func()

#___________________________________ If user select student version

while student_or_staff == "0":
    credit_input_func()
    #check_total()
    student_or_staff_func()
    if student_or_staff == "0":
        continue
    else:
        break

#___________________________________ If user select staff version

while student_or_staff == "1":
    print("____________________________________________________________________")
    print()
    print("                     Welcome to staff version")
    print("____________________________________________________________________")
    print()
    credit_input_func()
    #check_total()
    
    while True:
        print()
        enter_again = input("Would you like to enter another data set ('y' or 'q') ? ")
        print()
        if enter_again == "y":
            credit_input_func()
        elif enter_again == "q":
            print(all_result)
            break
    break

if student_or_staff == "q":
    print(all_result)



        
    

