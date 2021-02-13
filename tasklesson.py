def add_one(new_list, pos=0) -> list:
    idx = len(new_list) - 1 - pos
    if idx < 0:
        return [1] + new_list
    new_list[idx] += 1
    if new_list[idx] <= 9:
        return new_list
    else:
        new_list[idx] = 0
        return add_one(new_list, pos + 1)


assert add_one([9, 9]) == [1, 0, 0]
assert add_one([1, 2, 3]) == [1, 2, 4]

class Queue:
    def __init__(self):
        self.__ppl = []

def add(self, u): # O(1)
    self.__ppl.append(u)


def first(self): # O(1)
    if self.__ppl:
        return self.__ppl.pop
    return None
#пример Егорова Артема

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return power(x, n - 1) * x

x = int(input())
n = int(input())
print(power(x, n))