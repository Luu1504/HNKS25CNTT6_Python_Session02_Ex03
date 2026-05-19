
print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---")
name = input("Nhập họ và tên bệnh nhân: ")
patient_id = input("Nhập mã bệnh án: ")
examination_department = input("Nhập khoa/phòng khám: ")


print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")


examination_form = "Bệnh nhân: " + name + " - Mã BA: " + patient_id + " - Chuyển tới: " + examination_department

print(examination_form)