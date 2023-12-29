weight= int(input("Weight: "))
type_of_weight= input("(L)bs or (k)g ").lower()
if type_of_weight == "l":
    result= weight*0.45
    print(f"weight:{result}in Kg")
elif type_of_weight == "k":
    result= weight / 0.45
    print(f"weight:{result} in lbs")
else:
    print('type in between l,L or k,K')
