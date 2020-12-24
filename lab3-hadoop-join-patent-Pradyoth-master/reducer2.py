#!/usr/bin/env python
#Do a Join based on citing_id. This reducer gets the citing_id location
import sys
patent_dictionary = {}
last_citing_id = None
count = 0
citing_list = []
for line in sys.stdin:
    line = line.strip()
    try:
        splits = line.split('\t')
        if(len(splits) == 2):
            citing = splits[0]
            if not last_citing_id or last_citing_id == citing:
                last_citing_id = citing
                citing_list.append(splits[1])
            else:
                for citing2 in citing_list:
                    splts = citing2.split(',')
                    if(splts[1] in patent_dictionary.values()):
                        count = count+1
                print('%s,%s' %(last_citing_id,count))
                count = 0
                last_citing_id = citing
                citing_list = []
                citing_list.append(splits[1])
        else:
            citing = splits[0]
            patent_dictionary.clear()
            if not last_citing_id or last_citing_id == citing:
                patent_dictionary[splits[0]] = splits[1]
            else:   
                patent_dictionary[splits[0]] = splits[1]
                for citing1 in citing_list:
                    splts = citing1.split(',')
                    if(splts[1] in patent_dictionary.values()):
                        count = count + 1
                print('%s,%s' %(last_citing_id,count))
                count = 0
                last_citing_id = citing
                citing_list = []
    except:
        pass
