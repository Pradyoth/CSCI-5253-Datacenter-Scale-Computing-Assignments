
import sys
for line in sys.stdin:
    line = line.strip()
    splits = line.split(",")
    if len(splits) == 3:
        citing = splits[1]
        cited_and_state = splits[0] + ',' +splits[2]
        print('%s\t%s' %(citing,cited_and_state))

    else:
        patent_id = splits[0]
        location = splits[5]
        extra_field = splits[0]
        print('%s\t%s\t%s' %(patent_id,location,extra_field))





