inp = input("Mời người dùng nhập số")
num = []
while(inp != "0"):
    if inp.isdigit():
        num.append(inp)
    inp = input("Mời người dùng nhập số")
print(num)