# ASS 1
# WRITE A PYTHON PROGRAM TO GET 5 STUDENTS NAME FROM USER AND STORE IN LIST, DISPLAY 
# ALL THE STUDENTS NAME WITH UPPERCASE LETTERS 

# lst = []
# for i in range(5):
#     lst.append(input("Enter your name "))
# # print(lst)

# for name in lst:
#     print(name.upper())


# Problem 2
# WRITE A PYTHON PROGRAM TO GET 10 NUMBERS FROM USER, STORE IN A LIST,
# AND DISPLAY ONLY ODD NUMBER GETTING FROM LIST

# lst1 = []
# for i in range(10):
#     lst1.append(int(input("Enter your number here. ")))

# for num in lst1:
#     if num % 2 != 0:
#         print(num)

# Problem 3
# WRITE A PYTHON PROGRAM TO GET ANY WORD FROM USER, ITERATE THAT LIST TO 
# DISPLAY ONLY THOSE WORD NAME THAT START WITH "b".

# lst2 = []

# for i in range(5):
#     lst2.append(input("Enter your name "))
# # print(lst2)

# for x in lst2:
#    if x.startswith("b"):
#       print(x)
       

# Problem 4
# WRITE A PYTHON PROGRAM TO GET 10 NUMBER FROM USER, DISPLAY NUMBER THAT LESS
# 20 AND GREATER THAN 10.

num = []

for i in range(10):
    num.append(int(input("Enter your Number ")))
print(num)
    
for x in num:
    # x = int(x)
    if x > 10 and x < 20:
        print(x)