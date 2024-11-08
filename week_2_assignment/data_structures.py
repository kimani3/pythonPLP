my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)  

my_list[1]= 15

three_list = [60,50,70]
my_list.extend(three_list)
del my_list[-1]
my_list.sort()

index = my_list.index(30)
value= my_list[index]

print("index:", index,"value:", value)
print(my_list)