# Khai báo một đối tượng
car = {
    "brand": "Toyota",
    "year": 2018,
    "price": 13043.05,
    "color": ["red", "blue", "green"]
}

# Thêm mới khóa sound
car["sound"] = "Bose"

##### Xóa 1 khóa price
# del car["price"]
#car.pop("price")
# print(car) 


#### kiểm tra xem khóa đó có tồn tại bên trong Dict hay không
# if "acceleration" in car:
#     print(True)
# else: 
#     print(False)


### Sao chép một Dict
# car1 = car.copy()


#### Duyệt Dict theo key
# for key in car:
#     print(key) ### key: là khóa


#### Duyệt Dict theo value
for value in car.values():
    print(value)  #### 

