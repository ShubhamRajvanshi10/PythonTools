import os
with open ('uniqDll.txt', 'r') as Dl:
    for line in Dl:
        rec = line.strip()
	    NameWithoutDll , extra = rec.split('.dll')
	    print rec + "|" + NameWithoutDll + ";<.*>d__.*|MoveNext|0|0"
