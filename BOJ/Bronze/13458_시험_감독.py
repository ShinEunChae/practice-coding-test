N = int(input())
exams = list(map(int, input().split()))
over1, over2 = map(int, input().split())

exams = [exam - over1 for exam in exams]
answer = len(exams)

for exam in exams:
    if exam > 0:
        answer += (exam // over2)
        if exam % over2 != 0:
            answer += 1

print(answer)
