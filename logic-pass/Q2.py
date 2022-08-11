
#Q2/Write a program to find all prime numbers up to a given range of numbers?
#Ans
x= input('enter the lower value: ')
y= input('enter the upper value: ')
L = int(x)  
U = int(y)  
for n in range (L,U):  
    if n > 1:  
        for i in range (2,n):  
            if (n % i) == 0:  
                break  
        else:  
                print ('the prime number is ',n)  
                
