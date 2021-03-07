def check(string_1, string_2):
    if sorted(string_1.replace(' ', '').lower()) == sorted(string_2.replace(' ', '').lower()):
        print("Anagram")
    else:
        print("Sorry but not this time")


s1 = "listen"
s2 = "silent"
check(s1, s2)

s11 = "clint eastwood"
s22 = "old west action"
check(s11, s22)

s111 = "clint eastwwood"
s222 = "old west aaaction"
check(s111, s222)