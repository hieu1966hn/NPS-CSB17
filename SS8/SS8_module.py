##### Yêu cầu viết các hàm sau
def so_lon_hon(a, b):
    if a > b:
        return a
    elif a == b:
        return "Hai số bằng nhau"
    else:
        return b


def kiem_tra_chan_le(n):
    ## Kiểm tra n có phải là số nguyên hay không?
    if n % int(n) == 0:
        if n % 2 == 0:
            return "Chẵn"
        else:
            return "lẻ"


def kiem_tra_nam_nhuan(year):
    if year > 0:
        if year % 4 == 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


# arr = [1,2,3,4, "Hi", "Hello World!!",True, 100]


# def sum_array(arr):
#     tong = 0
#     for i in arr:
#         print(type(i) == "int")
#         if type(i) == "int":
#             print("vao for")
#             tong += i
#             print(tong)
#     return tong





def sap_xep_chuoi(input_string):
    ### Tách chuỗi thành các từ
    words = input_string.split(",") ### Array

    ### Xử lý khoảng cách thừa trong chuỗi: 
    # words2 = []
    # for word in words: 
    #     word = word.strip()
    #     words2.append(word)
    #### Cách 2
    for i in range(len(words)):
        words[i] = words[i].strip()
    
    ### Sx theo thứ tự bảng chữ cái
    words.sort()

    #### Kết hợp lại các phần tử trong mảng về thành 1 chuỗi ban đầu với dấu "," ngăn cách
    output_string = ",".join(words)
    return output_string


