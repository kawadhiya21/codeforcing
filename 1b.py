import math
import re

user_input = raw_input()
for x in xrange(0,int(user_input)):
    inp = raw_input()
    if inp[0] == 'R' and (inp[1].isalpha()==False) and (inp.count("C")==1):
        inp = inp.replace("R" , " ");
        inp = inp.replace("C" , " ");
        num = inp.split(" ");
        q = int(num[2])
        pre = "";
        while True:
            sperem = q%26
            if sperem==0:
                sperem = 26
                q = q-1
            if q!=0:
                pre += chr(64+sperem)
                q = q/26
            if q <= 0:
                break
        print (pre[::-1])+str(num[1])
    else:
        word = " ".join(re.findall("[a-zA-Z]+", inp))
        fin = 0
        length = len(word)
        for x in range(1,length+1):
            fin += ((int(ord(word[length - x])) - 64)*(26**(x-1)))
        print "R"+str((" ".join(re.findall(r'\d+', inp))))+"C"+str(fin)
