# print("hello")


# a=6;
# b=2;
# c=7;


# if a%2==1 and b>=1:
#     print(a%3)
#     print(b%a)
#     if c>=1 or b%a==0:
#         print("hello")
#     else:
#         print(b%a)    
# else:
#     print("hii")

# if b%2==0:
#     print(b+2)

# print(a%2==1 and b>=2)
# print(c%3>=1 and b>=2)
# print(a%2!=1 or c>=2)
# print(b%2<=3 and a>=2)
# print(a%2==2 or not b>=2)
# print(a%2==1 and b>=2)
# print(a%2)
# a+=3
# print(a)
# c-=2;
# print(a+b)
# print(c%2)
# print(c)
# print(a%c)



# for i in range(15,12,4):
#     print(i)




# for i in range(2,7,1):
#     if i%2==0 or i%3!=1:
#         print(i+2)
#         if i%3==1 and i%2==2:
#             print(i%3)
#         else:
#             print(i%3==0)    
#     else:
#         if i%3==1:
#             print(i-2)
#         else:
#             print(i-3)    
#         print(i-2)    



#! write a program to check user is eligible or not for voting
#? if user age is above 18 and below 40 and gender is male - eligible
#? if user age is above 18 and below 30 and gender is female - eligible

# gender="male"
# age=230

# if gender=="male":
#     if age>=18 and age<=40:
#         print("you are eligible for voting")
#     elif age>0 and age<100:
#         print("you are not eligible");
#     else:
#         print("enter valid age")
# elif gender=="female":          
#     if age>=18 and age<=30:
#         print("you are eligible for voting")
#     elif age>0 and age<100:
#         print("you are not eligible");
#     else:
#         print("enter valid age")
# else:
#     print("enter valid gender")        


# ? write a program to calcualte the total bill of the user . 
# ? if in case until is below 100 per unit charge is 5rs 
# ? and if above 100 and below 25o unit per unit charge is 8rs 
# ? and if above 250 unit per unit charge is 10rs 
# ? total bill is below 1000 not discount
# ? total bill is above 1000 and below 2500 5 discount
# ? total bill is above 2500 10 discount


# print the sum of digit in the number
# number=2341234;
# sum=0;
# while number>0:
#     digit=number%10;
#     sum+=digit;
#     number=number//100

# print(sum)    

# flag

# count=0;
# for num in range(1,11,1):

#     is_prime=True;

#     for i in range(2,num,1):
#         if num%i==0:
#             is_prime=False;
#             break;   

#     if is_prime:
#         count+=1;
#         print(num,"number is prime")
#     else:
#         print(num,"number is not prime")


# print("total 1 to 10 prime number is",count)

# write a program to print all prime number from 1 to 10;



# for i in range(1,4,1):
#     for j in range(2,6,2):
#         print(i+j)



# for i in range(5):
#     for j in range(5):
#         if   i==2  or j==2 :
#             print("* ",end="")
#         else:
#             print("  ",end="");    
#     print();    



# for i in range(5,10,1):
#     for j in range(5,i+1,1):
#         if j==5 or i==9 or i==j:
#             print("* ",end="")
#         else:
#             print("  ",end="")    
#     print()    

# num=16
# for i in range(num):
#     for j in range(num,i+1,-1):
#         print("  ",end="");
#     for k in range(0,i+1,1):
#         if i==num-1 or k==0 or k==i:
#             print("* ",end="")
#         else:
#             print("  ",end="")    
#     print();



# num = 9

# for i in range(5):
#     for j in range(i):
#         print("  ", end="")
#     for k in range(num - 2*i):
#         print("* ", end="")
#     print()


num = 9

# # Upper part
# for i in range(5):
#     for j in range(i):
#         print("  ", end="")
#     for k in range(num - 2*i):
#         print("* ", end="")
#     print()

# # Lower part (reverse)
# for i in range(4-1, -1, -1):
#     for j in range(i):
#         print("  ", end="")
#     for k in range(num - 2*i):
#         print("* ", end="")
#     print()



# num = 9
# total = 9   # total lines (5 up + 4 down)

# for i in range(total):

#     # Decide actual row index using condition
#     if i < 5:
#         spaces = i
#     else:
#         spaces = total - i - 1

#     # Print spaces
#     for j in range(spaces):
#         print("  ", end="")

#     # Print stars
#     for k in range(num - 2*spaces):
#         print("* ", end="")

#     print()


