# average height through loops

student_heights = input("Enter a list of student heights without a comma:").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


total_height = 0
for i in student_heights:
    total_height+=i
print(total_height)

student = 0
for students in student_heights:
    student +=1
print(student)

average_height = total_height/student
print(average_height)



# highest score using for loop

student_scores = input("Enter a list of student scores without a comma:").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score :
        highest_score=score
print(f'The highest score is: {highest_score}')


for i in range(1,11):        ##looping range
    print(i)
