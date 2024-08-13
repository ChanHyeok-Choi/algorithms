'''
큰 수의 법칙으로 풀어보는 **술에 취한 승객 문제** 풀이
문제상황: 100명이 탈 수 있는 비행기 좌석에 1번부터 100번까지의 승객이 자기의 번호표 순서대로 자리에 앉는다.
        그러나 하필 1번 승객이 술에 취해서 반드시 자기 번호가 아닌 다른 번호의 자리로 랜덤하게 앉게 된다.
        이 상황에서 100번의 승객이 100번 자리에 무사히 앉을 확률을 구하시오.
'''

from random import choice

def trial():
    occupied = [False] * 100
    seat_remainder = [i for i in range(100)]
    
    for i in range(99):
        if i == 0:
            seat_number = choice(seat_remainder[1:])
        elif occupied[i] == True:
            seat_number = choice(seat_remainder)
        else:
            seat_number = i
        occupied[seat_number] = True
        seat_remainder.remove(seat_number)
        
    return True if occupied[99]==False else False

number = [0, 0]

for i in range(1000000):
    number[trial()] += 1
    
print(number)