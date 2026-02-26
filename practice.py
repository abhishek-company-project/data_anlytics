

# for i in range(10,2,-2):

# for i in range(3,12,3):
#     print(i)


# # how many loop is itret   
# # starting point and end point   

# for i in range(15,5,-6):
#     print(i)

# num=3;
# for i in range(num):
#     for j in range(num):
#         if i==0 or j==0 or i==num-1 or j==num-1:
#             print("* ",end="")
#         else:
#             print("  ",end="")    
#     print()    



# num=5;
# for i in range(num):
#     for j in range(1+i):
#         if j==0 or i==0 or i==num-1 or i==j:
#             print("* ",end="")
#         else:
#             print("  ",end="")    
        
#     print()   
# 


# num=6;
# for i in range(num):
#     for j in range(num-1-i):
#         print("  ",end="")
#     for k in range(i+1):
#         if k==0 or i==0 or i==num-1 or k==i:
#             print("* ",end="")
#         else:
#             print("  ",end="")    
#     print()     


# write a program to print the total bill of the user
# if unit is below 100 per unt 5
# if total bill is below 1500 no discount
# 1500 - 2500 5%

# unit=176;
# total_bill=0;

# if unit<100:
#     total_bill=unit*5;
# elif unit>=100 and unit <= 250:
#     total_bill=unit*8;
# else:
#     total_bill=unit*10;

# if total_bill<1500:
#     print("total bill is ",total_bill)
# elif total_bill>1500 and total_bill<=2500:
#     total_bill-=total_bill*0.5
#     print("total bill is ",total_bill)    



# for i in range(1,7):
#     if i%2==1 and i>=3:
#         print(i%2)
#     elif i%2==0 or i>3:
#         print(i+2)    
#     else:
#         print(i-2)    