import json 
with open('sample-data.json') as exercise_json:
    data = json.load(exercise_json)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for i in data["imdata"]:
    print(i['l1PhysIf']['attributes']['dn'],'         ',i['l1PhysIf']['attributes']['descr'],'                  ',i['l1PhysIf']['attributes']['speed'],' ',i['l1PhysIf']['attributes']['mtu'])
    