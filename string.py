


# a="abhi"
# b="76"

# print(a[0]) # starting character
# print(a[len(a)-1])  # last character
# print(a[len(a)//2]) # mid character
# print(a[(len(a)-1)/2])




# str="my name is abhishek"

# #  get one by one all character
# #  check every character with a , e , i , o ,u
# # if not match count the total consonatcs


# for i in range(len(str)):
#     if str[i]!="a" and str[i]!="e" and str[i]!="o" and str[i]!="u" and str[i]!="i":
#         print(str[i])


# newstr="shanti"

# for i in range(len(newstr)-1,-1,-1):
#     print(newstr[i])





# str="Abhishek gurjar";
# newstr="";

# # string first character convert into upper case
# # find the space and convert next character to upper case in next itere

# space=False;
# for i in range(len(str)):
#     if i==0 or space==True:
#         newstr+=str[i].upper();
#         space=False;
#         continue;

#     if str[i]==" ":
#         newstr+=str[i]
#         space=True;

#     if str[i]!=" ":
#         newstr+=str[i]

# print(newstr)

# str="  shanti   infosoft      "
# print(str[:])
# print(str)
# print(str.strip())

# a = "Hello, Worhld!"
# print(a.replace("H", "J"))

# name="abhishek"
# age=23

# print("my name is",name,"i \xhh am old",age)
# print(f"my name is \'{name}\'.\fi am old {age}")

# report_content = "Section 1: Introduction\nThis is the first page content.\fSection 2: Detailed Analysis\nThis content starts on a new page (if printed)."

# with open("report.txt", "w") as file:
#     file.write(report_content)

# print("Report saved with form feed separators.")


# ! write a program to convert lower character to upper character and upper to lower
# ? str="ShANti InFOsoFT"

# get one by one all character
#  check character is upper so convert into lower
#  check character is lower so convert into upper

# A=65
# a=97

# 32

# str="ShANti InFOsoFT"
# newstr=""
# for i in range(len(str)):
#     char_code=ord(str[i])
#     if char_code>=65 and char_code<=90:
#         char_code+=32;
       
#         newstr+=chr(char_code)
#     elif char_code>=97 and char_code<=122:
#         char_code-=32;
#         newstr+=chr(char_code)    
#     else:
#         newstr+=chr(char_code)


# print(newstr)

# str="abc"
# print(ord(str[0]))



# text = "apple,banana,grape"
# print(text.split(" "))  

# print("4245".zfill(10))
# print("4512".center(10, "X"))

# print("hi".ljust(5, "-"))
# print("hi".rjust(5, "-"))
# print("hello".casefold())
# print("hello\tworld".expandtabs(3))



# count all characters in a string and show how many times each one appears

str="banana";

# get one by one character 
# check first in newstring you are all ready get count of the charaver
# put in new string for check next time 
# perticulater character count
# newstr=""
# for i in range(len(str)):
#     char=str[i];
#     check=False;
#     for k in range(len(newstr)):
#         if char==newstr[k]:
#             check=True;
#     if check==False:
#         newstr+=str[i];
#         count=0;
#         for j in range(len(str)):
#             if char==str[j]:
#                 count+=1;
#         print(char,count)


# str="bcdanana";

# for i in range(len(str)):
#     char=str[i];
#     exit=False;
#     for j in range(len(str)):
#         if char==str[j] and i!=j:
#             print(char)
#             exit=True;
#     if exit:
#         break;


#? Write a program to find the longest word in a sentence without using lists.


# str="my name is abhishek gurjar"
# count=0;
# for i in range(len(str)):
#     if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="u" or str[i]=="o": 
#         count+=1;
#     if str[i]==" ":
#         count+=1;
# print(count)
# print(len(str)-count)


#! Write a program to compress a string by counting consecutive characters.
#  Example:
#?  Input: "aaabbbbccdaa"
#?  Output: "a3b4c2d1a2"