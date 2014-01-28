max_users = int(raw_input())
user_input = [raw_input().split(' ') for x in range(0, max_users)]
 
user_records = {}
cummu_rec = []
 
for i in range(0, max_users):
    x, y = user_input[i]
    y = int(y)
    if x in user_records.keys():
        user_records[x] += y
    else:
        user_records[x] = y
    cummu_rec.append((x, user_records[x]))
        
mx = max(user_records.values())
 
for x, p in cummu_rec:
    if p >= mx and user_records[x] == mx:
        print x
        break