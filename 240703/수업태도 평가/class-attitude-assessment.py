import sys

student = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}

n = int(sys.stdin.readline().strip())

for _ in range(n):
    name, score = sys.stdin.readline().strip().split()
    student[name] += int(score)

sorted_student = sorted(student.items(), key=lambda item: item[1])

lowest_score = sorted_student[0][1]

num_lowest_scores = sum(1 for name, score in sorted_student if score == lowest_score)

score_list = []

for name, score in sorted_student:
    score_list.append(score)
    
if len(set(score_list)) == 1:
    print("Tie")
    exit()

second_score = sorted_student[num_lowest_scores][1]

num_second_scores = sum(1 for name, score in sorted_student if score == second_score)

if num_lowest_scores > 1 and num_second_scores < 2:
    print(sorted_student[num_lowest_scores][0])
elif num_second_scores > 1:
    print("Tie")
else:
    print(sorted_student[1][0])