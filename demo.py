# numbers = (1, 2, 3, 4, 5)
# products = ("P001","P002","P003")
# info = ("Văn Mỹ", 18, "Hết tiền", True)

# for index, value in enumerate(info, start=1):
#     print(f"..... {index}: {value}")


# for i in range(len(info)):
#     print(info[i])


# for item in info:
#     print(item)

# list_user = ("user001","user002","user003")

# users = {
#     "list_user[0]": {"Name":"Sang","age":19},
#     "list_user[1]": {"Name":"Khương","age":18},
#     "list_user[2]": {"Name":"Mỹ","age":90},
# }

# # print(users[list_user[0]]["Name"])
# print(users.get("list_user[0]").get("Name"))



# tạo một danh sách user
# thêm 5 phần tử vào danh sách.
# mỗi phần tử là 1 dictionary
# hiển thị toàn bộ thôn tin user ra màn hình


users = [
    {"id": "user001", "name": "Sang", "age": 19},
    {"id": "user002", "name": "Khương", "age": 18},
    {"id": "user003", "name": "Phú", "age": 90},
    {"id": "user004", "name": "Nhật", "age": 20},
    {"id": "user005", "name": "Duy", "age": 22}
]

print("Danh sách:")
for index, user in enumerate(users, start=1):
    print(f"{index}. {user["id"]}, {user["name"]}, {user["age"]}")