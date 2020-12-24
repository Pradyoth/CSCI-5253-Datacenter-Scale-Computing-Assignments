#Do a join based on the cited_id. This reducer gets the location of the cited_id
import sys
import string

last_cited_id = None
current_location = "-"
citing_id_list = []

for line in sys.stdin:
    cited, citing, location = [x.strip() for x in line.split('\t')]
    if not last_cited_id or last_cited_id == cited:
        last_cited_id = cited
        if location and location != "-":
            current_location = location
        else:
            citing_id_list.append(citing)
        # print ('%s\t%s\t%s' % (cited,cited,location))
    elif cited != last_cited_id:
        for citing1 in citing_id_list:
            print ('%s,%s,%s' % (last_cited_id,citing1,current_location))
        last_cited_id = cited
        current_location = "-"
        citing_id_list = []
        if location and location != "-":
            current_location = location
        else:
            citing_id_list.append(citing)

for citing1 in citing_id_list:
            print ('%s,%s,%s' % (last_cited_id,citing1,location))