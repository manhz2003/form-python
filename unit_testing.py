from DbManager import DbManager
from Admini import Admin

def main():
    db = DbManager()
    db.create_tables()

    # Tạo một instance Admin mới với username "admin" và password "123"
    admin = Admin("admin", "123")
    admin.register()

    # Xóa tất cả admin
    # admin.delete_all_admins()

    # Lấy và in ra tất cả thông tin admin (sẽ không có admin nào sau khi xóa)
    all_admins = admin.get_all_admins()
    for admin_info in all_admins:
        print("Thông tin Admin:", admin_info)

if __name__ == "__main__":
    main()