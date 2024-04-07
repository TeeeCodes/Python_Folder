weight = int(input("Weight: "))
weight_convert = input('(K)g or (L)bs: ')
kg = weight / float(0.45)
lbs = weight * float(0.45)


if weight_convert.upper() == "K":
    print("Weight in Lbs: " + str(kg))
else:
    print("Weight in Kg: " + str(lbs))
