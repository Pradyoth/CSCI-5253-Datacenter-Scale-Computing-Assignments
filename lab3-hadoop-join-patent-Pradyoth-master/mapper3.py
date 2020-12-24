import sys
for line in sys.stdin:
    line = line.strip()
    splits= line.split(",")
    if(len(splits)==2):
        citing_number = splits[0]
        count = splits[1]
        print('%s\t%s' %(citing_number,count))
    else:
        patent = splits[0]
        val = splits[1:22]
        print('%s\t%s' %(patent,val))
