def solution1(phone_book):
    # I don't like this method, because it uses sorting
    phone_book = sorted(phone_book)
    
    for z1, z2 in zip(phone_book, phone_book[1:]):
        if z2.startswith(z1):
            return False
    
    return True

print(solution1(["119", "2345", "119232141"]))

def solution2(phone_book):
    # This is a general solution, using hash_map
    hash_map = dict()
    
    for i in phone_book:
        hash_map[i] = 1
    
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    
    return True

print(solution1(["119", "2345", "119232141"]))