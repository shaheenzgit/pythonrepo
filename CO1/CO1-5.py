it100=list()
num_int=1
while num_int!=0:
    num_str=input("input an integer (0 terminates): ")
    num_int=int(num_str)
    if num_int<100:
        it100.append(num_int)
    else:
        it100.append("over")
print(it100)
