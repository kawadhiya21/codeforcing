user_input = raw_input()
inp = user_input.split(' ')
max_sum = 0;
scores = [];
min_sum = 0;
hours = 0;
for x in xrange(0,int(inp[0])):
    dh = raw_input()
    dh = dh.split(' ')
    max_sum += int(dh[1])
    min_sum += int(dh[0])
    new = [int(dh[0]),int(dh[1])]
    scores.append(new)    
if max_sum == int(inp[1]):
    print "YES"
    for x in scores:
        print x[1],
elif max_sum < int(inp[1]) or min_sum > int(inp[1]):
    print "NO"
else:
    hours = min_sum
    print "YES"
    for x in scores:
        if((hours + x[1] - x[0]) <= int(inp[1])):
            hours += x[1] - x[0]
            print x[1],
        elif hours == int(inp[1]):
            print x[0],
        elif((hours + x[1]) > int(inp[1])):
            print (x[0] + int(inp[1]) - hours),
            hours = int(inp[1])   



