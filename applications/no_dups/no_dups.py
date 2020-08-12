def no_dups(s):
    # Your code here
    d = set()
    s = s.split()
    for w in s:
        if w not in d:
            d.add(w)
    return d

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))