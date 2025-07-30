import re  # the search funtion
user_details = {}

# opens up 'user.txt' file to check login details
with open('user.txt', 'r') as f:
    for line in f:
        contents = line.strip()
        if "," in contents:
            contents = contents.split(",")
            if len(contents) == 2:
                username = contents[0].strip()
                password = contents[1].strip()
                user_details[username] = password

while True:
    print("Enter your login details")
    login_user = input("Enter your username:\n")
    login_pass = input("Enter you password:\n")

#checking if user login details correspond with those found in the file
    if login_user in user_details and user_details[login_user] == login_pass:
        print("Welcome to Task Manager!")
        break
    else:
        print("Invalid username or password.")

while True:
    menu = input("Select one of the following options:\n"
"r - register a user\n"
"a - add task\n"
"va - view all tasks\n"
"vm - view my tasks\n"
"ds - display statistics\n"
"e - exit\n").lower()
    
    if menu == "r":
        pass
        print("Register a user.")

        if login_user != "admin":
            print("Only the admin has permission to register users.")
            continue
        
        while True:
            #input must match the criteria set
            username = input("Create a new username. It must contain each of the following:\n" 
                             "- one upper case letter.\n"
                             "- one lower case.\n"
                             "- one number.\n"
                             "- length must be between 7-22.\n")
        
#creating a function that matches with the criteria set so that the machine can learn what is 
# required
            def valid_username(username): 
                if len(username) < 7 or len(username) > 22:
                    return False
                elif not re.search(r'[A-Z]', username):
                    return False
                elif not re.search(r'[a-z]', username):
                    return False
                elif not re.search(r'\d', username):
                    return False
                else:
                    return True
        
            #if it meets the criteria set pass through the loop
            if not valid_username(username): 
                print("Invalid username. It must contain atleast one of the following:\n"
                      "- upper case letter.\n"
                      "- one lower case.\n"
                      "- one number.\n"
                      "- length must be between 7-22.\n")
                continue
            else:
                break
            
        while True:    
            password = input("Create a new passwsord. It must contain each of the following:\n"
                             "- upper case letter.\n"
                             "- one lower case.\n"
                             "- one number.\n"
                             "- length must be between 8-16.\n"
                             "- one special character\n")
            
            #creating a function that checks if input meets criteria
            def valid_password(password): 
                if len(password) < 8 or len(password) > 16:
                    return False
                elif not re.search(r'[A-Z]', password):
                    return False
                elif not re.search(r'[a-z]', password):
                    return False
                elif not re.search(r'\d', password):
                    return False
                elif not re.search(r'[!,@,#,$,%,*,&,^,(,)]', password):#adding special characters
                    return False
                else:
                    return True
            
            if not valid_password(password):
                print("Invalid password. It must contain atleast one of the following:\n"
                      "- upper case letter.\n"
                      "- one lower case.\n"
                      "- one number.\n"
                      "- length must be between 9-22.\n"
                      "- one special character.\n")
                continue
            
            com_password = input("Comfirm your password:\n")
            if com_password != password:
                print("Passwords do not match.")
            else:
                break
        
        # checking if usename and password already exist
        if username or password in user_details:
            print("Username or password already exists.")
        
        # adding login details to user txt file
        with open('user.txt', 'a') as f: 
            f.write(f"\n")
            f.write(f"{username}, {password}\n")

    elif menu == "a":
        pass
        
        # function used to get current time
        from datetime import datetime 

        assign_user = input("Enter the username of indiviual task is assigned to:\n")
        while assign_user not in user_details:
            assign_user = input("Username cannot be found. Enter the username of the indiviual"
            " the task is assigned to:\n")
            
        task_title = input("Enter the title of the task assigned:\n")
        task_description = input("Enter the description of the assigned task:\n")
        assigned_date = datetime.today().strftime('%Y-%m-%d')
        due_date = input("Enter due date of the task:\n")
        task_complete = "No"
        
        with open('tasks.txt', 'a') as f:
                f.write("\n") # write inputs to file
                f.write(f"{assign_user}, Assigned initial tasks, {task_description}, {assigned_date}, {due_date}, {task_complete} \n")    
    
    elif menu == "va":
        pass
        with open('tasks.txt', 'r') as f:
            for line in f:
                contents = line.strip().split(",")
                print(",".join(contents))

    elif menu == "vm":
        pass
        with open('tasks.txt', 'r') as f:
            for line in f:
                contents = line.strip()
                if "," in contents:
                    contents = contents.split(",")
                    if login_user == contents[0]: # view tasks of person who has logged in
                        print(",".join(contents))

    elif menu == "ds":
        pass

        if login_user != "admin":
            print("Only admin can view statistics.")
            continue
        
        with open('user.txt', 'r') as f:
            total_users = sum(1 for _ in f) # count line of users

        with open('tasks.txt', 'r') as f:
            total_tasks = sum(1 for _ in f) # count line of tasks

        print(f"Total Users: {total_users}")
        print(f"Total Tasks: {total_tasks}")

    elif menu == "e":
        print("Goodbye.")    
        exit()

    else:
        print("Invalid option. Please choose from the menu.")