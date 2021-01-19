num= int(input("enter number :" ))

'''
ALAFIM=4
MEOT=5
ASAROT=6
YEHIDOT=7
x=num//1000
print("ALAFIM = " + str(x))
y=(num%1000)//100
print ("MEOT = " +str(y))
z=(num%100)//10
print ("ASAROT = " + str(z))
w=((num%100)%10)
print("YEHIDOT = " + str(w))
'''
print("ALAFIM = " + str(num//1000) + "\nMEOT =" + str((num%100)//100) + "\nASAROT = " + str((num%100)//10) + "\nYEHIDOT = " + str((num%100)%10))