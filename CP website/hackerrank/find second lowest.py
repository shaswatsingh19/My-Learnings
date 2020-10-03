n = int(input())

student = []

for i in range(n):
    student.append([input(),float(input())])

score = set([student[x][1] for x in range(n)])
score  = list(score)
score.sort()

# score[0] = lowest score
#score[1] = second lowest
#score[n] = largest
#x[0] = name
#x[1] = 37.21
# pick that one which x[1] is equal to score[1] == 37.21
student = [x[0] for x in student if x[1] == score[1]]

student.sort()

for s in student:
    print(s)
