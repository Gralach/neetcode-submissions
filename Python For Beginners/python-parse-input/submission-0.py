from typing import List

def read_integers() -> List[int]:
    check = str(input())
    return [int(x) for x in check.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
