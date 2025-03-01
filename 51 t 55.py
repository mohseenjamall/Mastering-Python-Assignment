# This file for the Assi 51 to 55 in lessons for Mastering Python

# numbers = [15, 81, 5, 17, 20, 21, 13]
# filtered_numbers = sorted([num for num in numbers if num % 5 == 0])
# for index, num in enumerate(filtered_numbers, start=1):
#     print(f"{index} => {num}")
# print("All Numbers Printed ✓") #Done


# for num in range(1, 21):
#     if num in [6,8,12]:
#         continue
#     print(f"{num:02d}")
# print("All Numbers Printed ✓") #Done

# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# rank_points = {
#     'A': 100,  
#     'B': 80,   
#     'C': 40    
# }
# total_points = sum(rank_points.get(rank, 0) for rank in my_ranks.values()) #check any errors
# for subject, rank in my_ranks.items():
#     if rank not in rank_points:
#         print(f"Invalid rank '{rank}' for {subject}")
#     else:
#         points = rank_points[rank] 
#         print(f"My Rank in {subject} Is {rank} And This Equal {points} Points")
# print(f"Total Points Is {total_points}") #Done

# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }
# rank_points = {
#     'A': 100,
#     'B': 80,
#     'C': 40,
#     'D': 20
# }
# for student in students:
#     print("------------------------------")
#     print(f"-- Student Name => {student}")
#     print("------------------------------")
#     total_points = 0 
#     for subject, rank in students[student].items():
#         subject_points = rank_points[rank] 
#         print(f"- {subject} => {subject_points} Points")
#         total_points += subject_points 
    
#     print(f"Total Points For {student} Is {total_points}")

# for student, subjects in students.items():
#     print("------------------------------")
#     print(f"-- Student Name => {student}")
#     print("------------------------------")
#     total_points = 0 
#     for subject, rank in subjects.items():
#         subject_points = rank_points[rank] 
#         print(f"- {subject} => {subject_points} Points")
#         total_points += subject_points  
#     print(f"Total Points For {student} Is {total_points}")
# print("------------------------------") #Done