def concatenate(s1: str, s2: str) -> str:
    ns = s1+s2
    if len(ns) > 10:
        return "Too long!"
    return ns



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
