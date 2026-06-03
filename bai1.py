# (1) Phân tích lỗi

# Tuple product_info ban đầu có bao nhiêu phần tử?
# 4 phần tử

# Phần tử "SP001" đang nằm ở index nào?
# Index 0

# Vì sao dòng sau lấy sai mã sản phẩm?
# product_code = product_info[1]
# Vì index 1 là "Áo polo nam", không phải mã sản phẩm

# Phần tử "Áo polo nam" đang nằm ở index nào?
# Index 1

# Vì sao dòng sau lấy sai tên sản phẩm?
# product_name = product_info[2]
# Vì index 2 là "Size L", không phải tên sản phẩm

# Vì sao dòng sau gây lỗi?
# product_length = product_info.length()
# Tuple không có phương thức length()

# Muốn đếm số phần tử trong tuple cần dùng hàm nào?
# len()

# Vì sao dòng sau không hợp lệ?
# product_info[3] = 279000
# Vì tuple là immutable (không thể thay đổi phần tử trực tiếp)

# Tuple có cho phép sửa trực tiếp phần tử không?
# Không

# Muốn cập nhật giá bán từ 299000 thành 279000 cần làm gì?
# Tạo một tuple mới với giá bán mới


# code sửa
product_info = ("SP001", "Áo polo nam", "Size L", 299000)
product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)
new_product_info = (
    product_info[0],
    product_info[1],
    product_info[2],
    279000
)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", new_product_info)