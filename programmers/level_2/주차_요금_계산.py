import math


def solution(fees, records):
    d = dict()
    for record in records:
        time, car, state = record.split()
        if car not in d.keys():
            d[car] = [time]
        else:
            d[car].append(time)
    d = dict(sorted(d.items()))

    for key, value in d.items():
        if len(value) % 2 == 1:
            value.append("23:59")

        intime = 0
        for i in range(0, len(value) - 1, 2):
            intime += (int(value[i+1][:2]) - int(value[i][:2])) * \
                60 + (int(value[i+1][3:]) - int(value[i][3:]))

        extra_fee = math.ceil((intime - fees[0]) / fees[2]) * fees[3]
        if extra_fee > 0:
            fee = fees[1] + extra_fee
        else:
            fee = fees[1]

        d[key] = fee

    return list(d.values())
