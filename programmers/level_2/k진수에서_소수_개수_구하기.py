def check_prime(check_num):
    if check_num == 1:
        return 0
    if check_num == 2:
        return 1
    for i in range(2, int(check_num**(1/2)) + 1):
        if check_num % i == 0:
            return 0
    return 1


def solution(n, k):
    number = ''
    while n > 0:
        n, r = divmod(n, k)
        number += str(r)
    number = number[::-1]

    answer = 0
    num = ''
    for i in range(len(number)):
        if number[i] != '0':
            num += number[i]
        else:
            if num:
                answer += check_prime(int(num))
                num = ''

    if num:
        answer += check_prime(int(num))

    return answer
