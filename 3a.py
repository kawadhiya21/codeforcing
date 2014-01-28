sq1 = raw_input()
sq2 = raw_input()

a1 = ord(sq1[0]) - 96
a2 = int(sq1[1])

b1 = ord(sq2[0]) - 96
b2 = int(sq2[1])

minimum = max(abs(a1-b1),abs(a2-b2))
print minimum

#one char move
one_char_move = abs(abs(a1-b1)-abs(a2-b2))
ver = a2-b2
hor = a1-b1
ocm = "";
if one_char_move > 0:
    if abs(ver) > abs(hor):
        if ver > 0:
            ocm = "D"
        else:
            ocm = "U"    
    else:
        if hor > 0:
            ocm = "L"
        else:
            ocm = "R"
for x in xrange(0,one_char_move):
    print ocm

#two character move

two_char_move = minimum - one_char_move
if two_char_move>0:
    if ver > 0:
        if hor > 0:
            tcm = "LD"
        elif hor < 0:
            tcm = "RD"
    else:
        if hor > 0:
            tcm = "LU"
        elif hor < 0:
            tcm = "RU"
for x in xrange(0,two_char_move):
    print tcm            