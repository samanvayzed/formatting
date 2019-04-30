import json

list_of_dicts = []
D={}
keys = [0,1,2]
values = [100,101,102]

#add a key and setup for a sub-dictionary

for i in range(3):
    D[i] = {}
    D[i]['x']=keys[i]
    D[i]['value']=values[i]
    list_of_dicts.append(D[i])


#print(list_of_dicts)

# convert into JSON:
json_dict = json.dumps(list_of_dicts)

# the result is a JSON string:
print(json_dict)



#print(D)
#add a sub-level to the dictionary
#if((D['a']).has_key('b') == 0)
#    D['a']['b'] = {}
