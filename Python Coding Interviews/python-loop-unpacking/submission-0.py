from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    cur_name, cur_max = "", 0
    for name, score in scores:
        if score > cur_max:
            cur_name = name
            cur_max = score
    return cur_name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
