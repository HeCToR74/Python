def compression(s):
    if s == '':
        return s
    else:
        new_s = ''
        for i in range(len(s)):
            if i == 0:
                k = 1
            else:
                if s[i] == s[i-1]:
                    k += 1
                else:
                    new_s += s[i-1] + str(k)
                    k = 1
        new_s += s[i] + str(k)
        if len(new_s) > len(s):
            return s
        else:
            return new_s


# Tests
# print(compression('aabcccccaaa'))  # 'a2b1c5a3'
# print(compression('abc'))  # 'abc'
# print(compression('abbbcccccccd'))  # 'abc'
# print(compression('aaaabcdeeee'))  # 'abc'
