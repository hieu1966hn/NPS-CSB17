# f = open('./SS12/example.txt', "x")
# ## Thêm nội dung vào file
# f.write("Hello World!!!")
# f.close()

## Đọc nội dung trong file
# f = open('./SS12/example.txt', "r")
# print(f.read())
# f.close()


## đếm số dòng trong file
# f = open('./SS12/example.txt', "r")
# ### Dùng vòng lặp để line by line
# i = 0
# for x in f:
#     # print(x)
#     i += 1
# f.close()
# print(f"Số dòng trong file example.txt là: {i}")


### Chữa bài 3a
# f = open("./SS12/numbers.txt", "w")
# ### Đoạn code thêm nội dung vào từng dòng trong 1 file
# f.write("1\n2\n3\n4\n5")
# f.close()

### Đọc các số từ file và tính tổng của chúng
# f = open("./SS12/numbers.txt", "r")
# total = 0
# line = 0
# for i in f:
#     i = int(i)  ## ép kiểu dữ liệu str -> int
#     total = total + i
#     line += 1
# print(f"Tổng các số trong file numbers.txt là: {total}")
# print(f"Giá trị trung bình của các số trong file numbers.txt là: {total/line}")
# f.close()


### Thực hành bài 4:
# def repace_word_in_file(input_file, output_file, target_word, replacement_word):
#     ## Đọc nội dung từ file đầu vào
#     with open(input_file,"r") as file:
#         content = file.read()
    
#     ### Thay thế từ mục tiêu -> từ khóa thay thế
#     new_content = content.replace(target_word, replacement_word)

#     ### Ghi nội dung vào file đầu ra
#     with open(output_file, "w") as file:
#         file.write(new_content)

#     print(f"Đã thay thế {target_word} bằng {replacement_word} trong file {output_file}")


# #### Chạy hàm
# repace_word_in_file('./SS12/sample.txt', "./SS12/sample_modified.txt", "Nguyen Trung Hieu", "Nguyễn Thế Vũ")


##### Bài 5: 