from time import sleep
print("The MENU is : " + "\n 1.insert number and ** by 3 " + "\n 2.insert 4 Ips to a list and print it " + "\n 3.insert 4 entries to DNS_Dictionary and print it " + "\n 4.check if a string is polindrom")
choice=input("enter your choise : ")
if(choice == "1"):
    num=int(input("enter your num : "))
    print("the exponent of your num is : "  + str(num ** 3))
elif(choice == "2"):
   # print("2")
    list=list()
    a=int(input("insert which ip it is : "))
    while(a <= 4 ):
        b=input("enter ip number " + str(a) +":")
        list.append(b)
        a +=1
    print(list)
elif(choice == "3"):
    #print("3")
    dict={}
    a=int(input("insert which DNS it is : "))
    while(a <= 4):
        b=input("enter URL number " +str(a) + ":")
        c=input("enter IP number " +str(a) + ":")
        dict.update({(b) : (c)})
        a +=1
    print(dict)
elif (choice == "4"):
    print("4")
    name=input("enter your word :")
    if(name == name[ ::-1]):
        print("its a polindrom")
    else:
        print("its isn't polindrom")
else:
    print("insert 1-4 only!!!")

