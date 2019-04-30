#for line in file_reader:
#      parts = line.split(" ")
#      line_tuple = (int(parts[0]), parts[1], int(parts[2]), int(parts[3]), float(parts[4]))
#      key = line_tuple[1]
#      outerdict[key] = innerdict 
 
#      innerdict["number"] = line_tuple[0]
#      innerdict["grade"] = line_tuple[2]
#      innerdict["total"] = line_tuple[3]
#      innerdict["weight"] = line_tuple[4] 

import json

temp = 1
num = 2
inner_dict = {}
outer_dict = {}
list_of_dicts = []
#l = [0,0,0,0,0]
keys=[0,1,2,3,4]
values=[100,101,102,103,104]
ld = {}

for x in range(5):
    print("NEW")
    outer_dict[x] = inner_dict
    print(ld)
    list_of_dicts.append(ld)
    print(list_of_dicts)
    
    inner_dict['x']=keys[x]
    print("WEN") 
    inner_dict['value']=values[x]
    #print(temp)
    #print(x)
    #print(l[x])
    print(outer_dict[x])
    ld = {}
    ld = outer_dict[x]
    

    #print(type(outer_dict[x]))
    #print(l)
 
    #print(outer_dict)    
    #temp = outer_dict[x]
    #print(temp)
    
    #list_of_dicts.append(ld)
   
    #print(list_of_dicts)

#print(l)

#print(outer_dict)

#print(outer_dict[0])
#print(outer_dict[1])

#list_of_dicts = []

#for x in range(num):
#    print("KKKKKK")
#    print(x)
#    print(outer_dict[x])
#    print("OOOOOO")
#    list_of_dicts.append(outer_dict[x])


print(list_of_dicts)


#list_of_dicts = [dict_0,dict_1,dict_2,dict_3,dict_4,dict_5,dict_6,dict_7]
#list_of_dicts = [dict_0,dict_1]


# convert into JSON:
#json_dict = json.dumps(list_of_dicts)

# the result is a JSON string:
#print(json_dict)

            
#print(outerdict[0])
#dict_0 = {}
#dict_0['x']=next_seven_days[0].strftime("%a")
#dict_0['value']=pred_result0


#dict_1 = {}
#dict_1['x']=next_seven_days[1].strftime("%a")
#dict_1['value']=pred_result1


