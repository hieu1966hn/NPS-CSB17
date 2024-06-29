### Khai báo một danh sách hoa quả;
# fruits = ["orange", "banana", "lemon", "strawberry"]

#### Số lượng phần tử trong list là: len(<list>)
# print(len(fruits)) # kq: 4

### Vị trí phần tử trong list: in ra phần tử có vị trí số 2.
# print(fruits[2]) ## Lemon


### In ra từng phần tử trong list Fruits. (R)
##C1
# for i in fruits:
#     print(i) ### i là: từng phần tử trong fruits.
##C2:
# for i in range(0, len(fruits)):
#     print(fruits[i]) ### i là: Vị trí phần tử trong fruits

### Thêm một phần tử vào cuối List: append()
# fruits.append("grape")
# print(fruits)

### chèn một phần tử vào vị trí chỉ định: insert
# fruits.insert(1, "watermelon")
# print(fruits)

### Update 1 phần tử khi biết vị trí phần tử đó:
# fruits[2] = "kiwi"

### Xóa 1 phần tử trong list khi biết tên phần tử đó: remove
# fruits.remove("strawberry")
# fruits.remove(fruits[5])


#### Xóa toàn bộ phần tử trong list: list.clear()
# fruits.clear()
# print(fruits)


##### Tìm kiếm phần tử nằm trong list: tìm grape và in ra vị trí của nó: list.index(<item>)
# fruit = "banana"
# if fruit in fruits: # True có nằm trong list.
#     position_grape = fruits.index("grape")
#     print(position_grape)
# else:
#     print(f"there have no {fruit} in fruits")


#### Sao chép 1 list:
# list1 = [1,2,"Hi", "hello", 100]
# list2 = list1
# list2[4] = 1000
# print(list1)

### Sử dụng phương thức copy().
# list1 = [1,2,"Hi", "hello", 100]
# list2 = list1.copy()
# list2[4] = 1000
# print(list1)


###### Khai báo kiểu dữ liệu tuple
tuple1 = (1, 2, 3, 4, 5)
### thêm mới phần tử vào tuple
# tuple1.append(10) ### không thêm được phần tử.

### update phần tử trong tuple (không thể)
# tuple1[0] = 0


#### Duyệt phần tử bên trong tuple1 với vòng for
# for i in tuple1:
#     print(i)
