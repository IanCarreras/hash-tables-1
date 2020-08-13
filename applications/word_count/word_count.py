def word_count(s):
    # split string into array of words
    # iterate over array creating a hashtable with word as key and count as value
    d = {}
    s = s.split('[":;,.-+=/\|[]{}()*^&]')
    for w in s:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return s


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))