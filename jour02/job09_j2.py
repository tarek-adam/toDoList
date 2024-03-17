x = 1
New_Liste = []
Liste = [10,20,30,20,10,50,60,40,80,50,40]

for num in Liste:
    if num not in New_Liste:
        New_Liste.append(num)
print(New_Liste)