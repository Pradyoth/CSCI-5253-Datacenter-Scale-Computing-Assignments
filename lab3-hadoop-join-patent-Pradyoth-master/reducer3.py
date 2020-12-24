import sys
citing_dictionary = dict()
patent_dictionary= dict()
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    if(len(splits) == 2):
        citing_id = splits[0]
        count = splits[1]
        citing_dictionary[citing_id] = count    
    else:
        patent_id = splits[0]
        patent_dictionary[patent_id] = splits[1:22]

for key,value in citing_dictionary.items():
        if key in patent_dictionary:
             patent_dictionary[key].append(value)

for key,value in patent_dictionary.items():
    print(key,value)
