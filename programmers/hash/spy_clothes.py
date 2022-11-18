def solution1(clothes):
    answer = 1
    hash_map = dict()
    for li in clothes:
        if li[1] not in hash_map:
            list = []
            hash_map[li[1]] = list
            hash_map[li[1]].append(li[0])
        else:
            hash_map[li[1]].append(li[0])

    for i in hash_map:
        answer *= len(hash_map[i]) + 1

    return answer - 1

def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

# I first meet Counter module and reduce function
### practice ###
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]

def practice(users):
    from collections import Counter
    from functools import reduce
    
    cnt = Counter("hello world!") # output : Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
    print(cnt)
    
    sum_age = reduce(lambda x, y: x + y['age'], users, 0)
    return sum_age

print(practice(users)) # output : 227