from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    answer = 0

    if (s1 + s2) % 2 != 0:
        return -1

    for _ in range(len(q1) * 4):
        if s1 == s2:
            return answer
        elif s1 > s2:
            e = q1.popleft()
            q2.append(e)
            s1 -= e
            s2 += e
            answer += 1
        elif s1 < s2:
            e = q2.popleft()
            q1.append(e)
            s1 += e
            s2 -= e
            answer += 1

    return answer if s1 == s2 else -1

# 시간 초과 코드

# from collections import deque

# def solution(queue1, queue2):
#     q1 = deque(queue1)
#     q2 = deque(queue2)
#     answer = 0

#     if (sum(q1) + sum(q2)) % 2 != 0:
#         return -1

#     for _ in range(len(q1) * 4):
#         s1 = sum(q1)
#         s2 = sum(q2)
#         if s1 == s2:
#             return answer
#         elif s1 > s2:
#             e = q1.popleft()
#             q2.append(e)
#             answer += 1
#         elif s1 < s2:
#             e = q2.popleft()
#             q1.append(e)
#             answer += 1

#     return answer if sum(q1) == sum(q2) else -1
