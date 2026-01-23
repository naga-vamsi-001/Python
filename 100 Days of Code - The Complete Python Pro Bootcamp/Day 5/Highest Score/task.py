student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
print(total_score) # Using built in function

sum = 0
for score in student_scores:
    sum += score
    print(sum) #To the items in list using for loop

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(max(student_scores))

#MAX
Max_num = student_scores[0]
for score in student_scores:
    if score > Max_num:
        Max_num = score

print(Max_num)

#Min
min_number = student_scores[0]
for score in student_scores:
    if score < min_number:
         min_number = score
print(min_number)