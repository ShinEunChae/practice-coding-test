from itertools import product


def solution(users, emoticons):
    discounts = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    answer = [0, 0]

    for discount in discounts:
        signup = 0
        payment = 0

        for user in users:
            pay = 0
            for i in range(len(discount)):
                if discount[i] >= user[0]:
                    pay += emoticons[i] * (100 - discount[i]) / 100
                    if pay >= user[1]:
                        signup += 1
                        pay = 0
                        break
            payment += pay

        if signup > answer[0] or (signup == answer[0] and payment > answer[1]):
            answer = [signup, payment]

    return answer
