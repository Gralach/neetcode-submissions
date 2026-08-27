from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    check = {}
    for i in word:
        if i not in check:
            check[i] = 0
        check[i] += 1
    return check

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
