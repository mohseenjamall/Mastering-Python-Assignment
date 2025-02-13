# This file for the Assi 47 to 50 in lessons for Mastering Python

# num = input("Please enter a positive integer: ")
# if num.isdigit() and int(num) > 0:
#     num = int(num)
#     count = 0
#     i = num - 1
#     while i > 0:
#         if i == 6:
#             i -= 1
#             continue
#         print(i)
#         count += 1
#         i -= 1
#     print(f"All numbers have been printed successfully! Total numbers printed: {count}")
# else:
#     print("Invalid input! Please enter a positive integer greater than 0.") # Done


# friends = ["Mohamed", "Shady", "ahmed", "huda", "Sherif"]
# iNdex = 0
# iGnoredCount = 0
# while iNdex < len(friends):
#     name = friends[iNdex]
#     if name[0].islower():
#         iGnoredCount += 1
#     else:
#         print(name)
#     iNdex += 1 
# print(f"Number of ignored names: {iGnoredCount}") # Done


# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
# while skills:
#     print(skills.pop(0)) # Done


# myFriends = []
# count = 4
# while len(myFriends) < count:
#     fName = input("inter your freind name: ").strip()
#     if fName.isupper():
#         print("Invalid name! The name cannot be all uppercase.")
#         fName = fName.lower().capitalize()
#     else:
#         if fName.islower():
#             fName = fName.capitalize()
#             print(f"Name '{fName}' was converted to capitalize.")
#     myFriends.append(fName)
#     print(f"'{fName}' has been added to the list.")
#     count -= 1
#     print(f"Remaining slots: {count}")
#     print("\nYour friends list is now full:")
#     print(myFriends) #Done