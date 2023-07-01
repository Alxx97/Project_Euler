#Excercise 1: This program shows you the sum of the multiples of 3 and 5 below a given number
def Sum_of_multiples_3And5(number):
    s = 0
    for i in range(number):
        if i%5==0:
            s = s + i
        elif i%3==0:
            s = s + i
    return s    


for i in [543,233168,16687353,89301183]:
    print(Sum_of_multiples_3And5(i))