list = [1,1,1,1,1,1,2,2,2,2,2,4,4,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,8,8,9,9,9]

y = ''

for x in range(0, len(list)):
    
    if y != list[x]:
        print(y)
        y = list[x]
    