#List Names
admin = ["Mohsen","Menna","Huda","samer","Ahmed"]

#Login
name = str(input("Please Type Your Name: ").strip().capitalize())

if name in admin:
    print(f"Welcome Back {name}")
    
    option = str(input("Choose what you need (Update (U) or Delete (D))!! ").strip().lower())
    
    if option == "update" or option == "u":
        newName = str(input("Type New Name: ").strip().capitalize())
        admin[admin.index(name)] = newName
        print(f"Name is Updated, Welcome {newName}")
        # print(admin)
        
    elif option == "delete" or option == "d":
        admin.remove(name)
        print(f"Name is Deleted, ({name})")
        # print(admin)
        
    else:
        print("wrong option choosed".capitalize())
        
else:
    print("you are not admin bitch \n".capitalize())
    
    status = input("Add You!! (Y, N) ").strip().capitalize()
    
    if status == "Yes" or status == "Y":
        admin.append(name)
        print(f"Name is Updated, Welcome {name} \n")
        # print(admin)
        print("we're add you bitch, don't do it again \n".capitalize())
        
    else:
        print("you are not add bitch".capitalize())