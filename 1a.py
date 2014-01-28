import math
user_input = raw_input()
inp = user_input.split(' ')
print int(math.ceil(float(inp[0])/float(inp[2])) *  math.ceil(float(inp[1])/float(inp[2])))
#print math.ceil(s1/l) + math.ceil(s2/l)

