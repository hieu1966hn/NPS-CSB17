## ví dụ với vòng lặp for trong Python
## Đề bài: In ra các số lẻ từ phạm vi 10 - 50.
# for i in range(11, 50, 2):
#     print(i)

## Ví dụ với while: Nhưng bỏ đi không in ra số 19
# n = 11
# while n <= 50:
#     if n == 19:
#         n = n + 2
#         continue
#     print(n)
#     n = n + 2


#### Chữa bài 1 ý c.
# for i in range(9, 4, -1):
#     print(i) ## 9 -> 5
#     if i == 5:
#         for k in range(10, 13):
#             print(k)

#### Chữa bài 2 ý
# for i in range(21):
#     if i % 3 == 0:
#         print(i)


#### Chữa bài 3
# n = int(input("Mời người dùng nhập vào n")) # -3
# while n < 0 or n != float(n):
#     print("Số chưa thỏa mãn yêu cầu đề bài, mời nhập lại!")
#     n = int(input("Mời người dùng nhập vào n")) #5
#     for i in range(n):
#         print(i)
#     break


#### Chữa bài 4: Coi như xong bước kiểm tra số âm ở bài 3;
n = int(input("Mời người dùng nhập vào n "))  # 1234// 10 => 123
so_chu_so = 1
while n // 10 > 0:
    n = n // 10 # 123 #12 #1 #0
    so_chu_so += 1 #2 #3 #4

print(so_chu_so)



#### Chữa bài 5: di chuyển sang turtle online để làm cho dễ.
