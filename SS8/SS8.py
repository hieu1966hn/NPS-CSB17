#### Khai báo hàm sayHello.
# def sayHello():
#     # print("Hello World!!!")
#     return "Hello World!!!"
#     print("Đây là nội dung sau lệnh return")

### Gọi hàm: 
# sayHello()
# print(sayHello()) ### ? 


import SS8_module
###### Giải bài tập thực hành với module

### Giải bài 1: 
a = 1
b = 2
print(f"Số lớn hơn giữa {a} và {b} là: {SS8_module.so_lon_hon(a,b)}") # 

### Giải bài 2: 
print(f"{b} là số {SS8_module.kiem_tra_chan_le(b)}")

### Giải bài 3: 
year_input = 2024
flag = SS8_module.kiem_tra_nam_nhuan(year_input)
if flag == True:
    print(f"{year_input} là năm nhuận")
else:
    print(f"{year_input} là không là năm")

### Giải bài 4: 
# arr = [1,2,3,4, "Hi", "Hello World!!",True, 100]
# print(f"Tổng của mảng là: {SS8_module.sum_array(arr)}")


#### Giải bài 5: 
chuoi = "Du, Lâm, Vũ, Khánh, Phong"
print(f"Chuỗi sau khi sx là: {SS8_module.sap_xep_chuoi(chuoi)}")
