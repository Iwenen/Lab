import re
with open('row.txt', 'r', encoding='utf-8') as file:
    g = file.read()
    
# 1
# pattern = r'[а-яА-Я]+а[0б*][а-яА-Я]*'
# founded = re.findall(pattern, g)
# print(founded)

# 2
# pattern = r'xаб{2,3}+[а-яА-Я]*'
# founded = re.findall(pattern, g)
# print(founded)

# 3 
# pattern = r'[а-я]+-[а-я]+'
# founded = re.findall(pattern, g)
# print(founded)

# 4
# pattern = r'[А-Я]+[а-я]+'
# founded = re.findall(pattern, g)
# print(founded)

# 5
# pattern = r'[а-яА-Я]+а.+б$'
# founded = re.findall(pattern, g)
# print(founded)  

# 6
# sub = re.sub(r' ', ',', g)
# sub = re.sub(r'\.', ':', g)
# print(sub)

# 7
# sub = re.sub(r'[а-яА-Я]+_[а-яА-Я]', r'[А-Я]*[а-я]+[А-Я][а-я]*', g)
# print(sub)

# 8
# sub = re.sub(r'(?<!^)(?=[A-ZА-Я])', ' ', g)
# print(sub)

# 9
# sub = re.sub(r'(?<!^)(?=[A-ZА-Я])', ' ', g)
# print(sub)

# 10
# sub = re.sub(r'[А-Я]*[а-я]+[А-Я][а-я]*', r'[а-яА-Я]+_[а-яА-Я]', g)
# print(sub)
