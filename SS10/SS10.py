# Khai báo một đối tượng
# car = {
#     "brand": "Toyota",
#     "year": 2018,
#     "price": 13043.05,
#     "color": ["red", "blue", "green"]
# }

# Thêm mới khóa sound
# car["sound"] = "Bose"

##### Xóa 1 khóa price
# del car["price"]
# car.pop("price")
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
# for value in car.values():
# print(value)  ####


Ninja = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "level": 2,
}

## thêm 50 tiền cho nhân vật
Ninja["Gold"] += 50

Ninja["Backpack"].append("FlintStone")

#### Yêu cầu đặc biệt: viết hàm tăng x2 chỉ số khi nhân vật đạt level 5.
def level_up(ninja):
    if ninja["level"] >= 5:
        for key in ninja:
            # print(ninja[key] *2)
            if str(ninja[key]).isdigit(): ## ép kiểu sang chuỗi để kiểm tra có phải là số?
                if ninja[key] != ninja["Age"] and ninja[key] != ninja["level"]:
                    ninja[key] *= 2
    return ninja

## Tăng level lên 5
Ninja["level"] = 5
print(level_up(Ninja)) ### 