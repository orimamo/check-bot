list=[]
# print(list)
for i in range(10):
    a=int(input("insert number : "))
    list.insert(i,a)
    i +=1
num=0
for i in range(len(list)):
    num=num+list[i]
print(num)
print(list)