import math
### Câu điều kiện
# a = 500
# b = 400
# if a < b:
#     print(f"{a} nhỏ hơn {b}")
# elif a>b:
#     print(f"{a} lớn hơn {b}")
# else:
#     print(f"{a} bằng {b}")




#### Bài thực hành 1: 
# a = float(input("Nhập vào số đầu tiên: "))
# b = float(input("Nhập vào số thứ hai: "))
# c = float(input("Nhập vào số thứ ba: "))
# if a>b and a>c:
#     print(f"{a} là số lớn nhất")
# elif b>a and b>c:
#     print(f"{b} là số lớn nhất")
# else:
#     print(f"{c} là số lớn nhất")

### Bài 2:
# kg = float(input("Mời người dùng nhập cân nặng(kg): "))
# m = float(input("Mời người dùng nhập chiều cao(m): "))
# BMI = kg/(m*m)
# print(BMI)

#### Bài 3: 1 -2 1
# a = float(input("Mời người dùng nhập số a: "))
# b = float(input("Mời người dùng nhập số b: "))
# c = float(input("Mời người dùng nhập số c: "))

### Nghiệm của Pt bậc 2;
# delta = b*b-4*a*c
# x1 = (-b + math.sqrt(delta))/(2*a)
# x2 = (-b - math.sqrt(delta))/(2*a)
# print(f"Vậy nghiệm của pt bậc 2 với x1 = {x1} và x2 = {x2}")



#### bài 7:
# ch = "h"
# if ch.isalpha() == True:
#     print(f'{ch} là ký tự trong bảng chữ cái')


#### Bài 9
# a = "hello world"
# b = a.split("hello ")
# print(b)

### Bài 8:
a = input("Nhập vào một số: ")
if a.isdigit():
    print(f"Chuỗi {a} là một số")
else:
    print(f"Chuỗi {a} không là một số")
