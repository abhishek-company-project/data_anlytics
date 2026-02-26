# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)


# Rotate a list to the right by k positions

# num = [1, 5, 4, 8, 6, 3]
# k = 5

# for i in range(len(num)-k):
#     num+=[num[i]];

# print(num)


# num = [1, 2, 5, 4, 8, 6, 3]
# k = 5

# n = len(num)
# k = k % n

# for i in range(k):
#     last = num[n-1]   # store last element
    
#     # shift elements to right
#     j = n - 1
#     while j > 0:
#         num[j] = num[j-1]
#         j -= 1
    
#     num[0] = last   # put last element at front

# print(num)


student = {
    "student_id": "STU10234",
    "personal_info": {
        "first_name": "Rahul",
        "last_name": "Sharma",
        "gender": "Male",
        "age": 21,
        "date_of_birth": "2004-05-14",
        "contact": {
            "email": "rahul.sharma@email.com",
            "phone": "9876543210",
            "address": {
                "street": "MG Road",
                "city": "Indore",
                "state": "Madhya Pradesh",
                "pincode": "452001"
            }
        }
    },
    
    "academic_info": {
        "course": "B.Tech",
        "branch": "Computer Science",
        "year": 3,
        "semester": 6,
        "roll_number": "CSE20230045",
        "subjects": [
            {"name": "Data Structures", "code": "CS301", "marks": 85},
            {"name": "Operating System", "code": "CS302", "marks": 78},
            {"name": "Database Management", "code": "CS303", "marks": 88},
            {"name": "Computer Networks", "code": "CS304", "marks": 81}
        ]
    },
    
    "attendance": {
        "total_classes": 120,
        "attended": 102,
    },
    
    "skills": [
        "Python",
        "Java",
        "React",
        "SQL"
    ],
    
    "projects": [
        {
            "title": "Student Management System",
            "technology": "Python, MySQL",
            "duration": "3 months"
        },
        {
            "title": "E-commerce Website",
            "technology": "React, Node.js",
            "duration": "4 months"
        }
    ],
    
    "status": "Active"
}

# if student["attendance"]["total_clasees"]>=100 :
#     if  student["attendance"]["attended"]>=80:
#         print("eligible")
#     else:
#         print("not eligible")    
# elif  student["attendance"]["total_clasees"]>=100 and student["attendance"]["attended"]<=80:
#     print("not eligible")   


# for skill in student["skills"]:
#     print(skill[0])

print(student["personal_info"]["contact"]["address"]["city"])
# sum=0;
# for i in student["academic_info"]["subjects"]:
#    sum+= i["marks"]

# print(sum)
# for i in student["projects"]:
#     print(i["technology"].split(",")[0])


company = {
    "employees": {
        "E101": {
            "name": "Rahul Sharma",
            "department": "IT",
            "salary": 55000,
            "skills": ["Python", "SQL", "React"],
            "projects": ("Ecommerce", "Dashboard")
        },
        "E102": {
            "name": "Neha Verma",
            "department": "Sales",
            "salary": 48000,
            "skills": ["Excel", "Communication"],
            "projects": ("Leads",)
        },
        "E103": {
            "name": "Amit Singh",
            "department": "IT",
            "salary": 62000,
            "skills": ["Python", "Django", "AWS"],
            "projects": ("API", "Cloud")
        },
        "E104": {
            "name": "Priya Patel",
            "department": "HR",
            "salary": 45000,
            "skills": ["Communication", "Management"],
            "projects": ("Hiring",)
        }
    },

    "products": {
        "P201": {
            "name": "Laptop",
            "price": 55000,
            "stock": 10,
            "sold": [2, 1, 3, 2]
        },
        "P202": {
            "name": "Mouse",
            "price": 700,
            "stock": 50,
            "sold": [5, 8, 6, 10]
        },
        "P203": {
            "name": "Keyboard",
            "price": 1500,
            "stock": 30,
            "sold": [3, 4, 2]
        }
    },

    "customers": {
        "C301": {
            "name": "Arjun",
            "city": "Indore",
            "purchases": ["Laptop", "Mouse"],
            "amount": (55000, 700)
        },
        "C302": {
            "name": "Simran",
            "city": "Bhopal",
            "purchases": ["Keyboard"],
            "amount": (1500,)
        },
        "C303": {
            "name": "Rohit",
            "city": "Delhi",
            "purchases": ["Laptop", "Keyboard"],
            "amount": (55000, 1500)
        }
    }
}

# company["employees"]["E101"]["salary"]=150000

# print(company)

# for emp in company["employees"]:
#     print(company["employees"][emp]["salary"])

# max=0;
# name="";
# for emp in company["employees"].values():
#     if emp["salary"]>max:
#      max=emp["salary"]
#      name=emp["name"]

# print(name)


# number={};

# for i in range(10):
#     if i%2==0:
#         number[i]=i*i;

# print(number)

# number={i:i*i for i in range(5) if i%2==0}
# print(number)


# 🔹 What is an Expression in Python?
# ✅ Definition:

# An expression is anything that:

# Produces a value

# Can be evaluated (Python calculates it)

# 👉 Expression always gives a result.

# ✅ Examples of Expressions
# 5 + 3

# ✔ Output: 8

# 10 > 5


# 🔹 What is a Statement in Python?
# ✅ Definition:

# A statement is an instruction that Python executes.

# 👉 A statement performs an action.

# ✅ Examples of Statements
# x = 10

# Assignment statement

# if x > 5:
#     print("Big")

# If statement

# for i in range(5):
#     print(i)


# 🔹 What is List Comprehension?

# It is a short and clean way to create lists.

# 🔹 Basic Syntax
# [expression for item in iterable]
# ✅ Example 1: Square Numbers
# Normal way (using loop)
# numbers = []
# for i in range(5):
#     numbers.append(i*i)

# print(numbers)
# Using List Comprehension
# numbers = [i*i for i in range(5)]
# print(numbers)

# Output:

# [0, 1, 4, 9, 16]
# ✅ Example 2: With Condition
# even_numbers = [i for i in range(10) if i % 2 == 0]
# print(even_numbers)

# Output:

# [0, 2, 4, 6, 8]






# 2️⃣ Set Comprehension
# 4
# 🔹 Syntax
# {expression for item in iterable}
# ✅ Example 1: Square Numbers (No duplicates)
# numbers = {i*i for i in range(5)}
# print(numbers)

# Output:

# {0, 1, 4, 9, 16}
# ✅ Example 2: Remove Duplicates
# nums = [1, 2, 2, 3, 3, 4]

# unique = {x for x in nums}
# print(unique)

# Output:

# {1, 2, 3, 4}


# 3️⃣ Dictionary Comprehension
# 🔹 Syntax
# {key_expression: value_expression for item in iterable}
# ✅ Example 1: Number and Square
# squares = {i: i*i for i in range(5)}
# print(squares)

# Output:

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# ✅ Example 2: With Condition
# even_squares = {i: i*i for i in range(10) if i % 2 == 0}
# print(even_squares)

# Output:

# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}






# 🎯 Real-World Example

# Convert list of names to uppercase:

# names = ["john", "alice", "bob"]

# upper_names = [name.upper() for name in names]
# print(upper_names)

# Output:

# ['JOHN', 'ALICE', 'BOB']