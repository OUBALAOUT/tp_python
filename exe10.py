def fusionner_dicts(dict1,dict2):
  for i in dict1:
    if dict1[i] == dict2[i]:
       return dict1 | dict2
print(fusionner_dicts({'pomme':12,'tomate':10},{'pomme':12,'kiwi':3}))

