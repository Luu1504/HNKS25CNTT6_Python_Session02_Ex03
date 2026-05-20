full_name = input("Họ và tên của bệnh nhân: ")
patient_age = int(input("Tuổi của bệnh nhân: "))

if full_name.strip() == "" or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else:
    if patient_age < 6:
        result =  "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif patient_age >= 80:
        result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

  


print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(f"Họ và tên: {full_name}")
print(f"Tuổi: {patient_age}")
print(f"Kết quả phân luồng {result}") 