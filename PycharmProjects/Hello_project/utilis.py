
def find_max(list):
    max= list[0]
    for numbers in list:
        if numbers > max:
            max= numbers
    print (max)