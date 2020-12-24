import sys
for line in sys.stdin:
    # Setting some defaults
    citing = "-"
    cited = ""
    location = "-"
    line = line.strip()
    splits = line.split(",")
    if len(splits) == 2: # Transactions have more columns than users
        citing = splits[0]
        cited = splits[1]
    else:
        cited = splits[0]
        location = splits[5]                  
    print ('%s\t%s\t%s' % (cited,citing,location))