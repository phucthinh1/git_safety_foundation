def phep_tinh():
    print("Chọn phép tính:")
    print("1. Cộng (+)")
    print("2. Trừ (-)")
    print("3. Nhân (*)")
    print("4. Chia (/)")

    lua_chon = input("Nhập lựa chọn của bạn (1/2/3/4): ")
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))

    if lua_chon == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif lua_chon == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif lua_chon == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif lua_chon == '4':
        if num2 == 0:
            print("Không thể chia cho số 0!")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Lựa chọn không hợp lệ.")

phep_tinh()
