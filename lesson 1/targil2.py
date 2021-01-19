print("tomato cost - 3 NIS " + "\ncucumber cost - 4 NIS" + "\ncola cost - 5 NIS" + "\nchicken cost - 20 NIS")

a=int(input("how much tomato you want:")) *3
b=int(input("how much cucumber you want:")) *2
c=int(input("how much kola you want:")) *5
d=int(input("how much chicken you want:")) *20
print("before tax : " + str(a + b + c + d) + " NIS")
print("after tax : " + str("%.1f" % ((a+b+c+d)*1.17)) + " NIS")