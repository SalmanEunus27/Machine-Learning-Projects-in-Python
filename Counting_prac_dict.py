name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    email = line.split()
    if len(email)<1:
        continue
    if email[0]!= 'From':
        continue
        
    else:
        d = email[0:]
        c = email[1]
    print(d)
        
    print(c)
            
    for c in d:
        counts[c] = counts.get(c,0)+1
    
    
   
    
bigcount = None
bigword = None
for c,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = c
        bigcount = count


#print(bigword,bigcount)