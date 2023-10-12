from aeroport import *

airport = Airport("Tashkent International Airport", "Tashkent")
management = boshqaruv('Dadaxon',airport)

while True:
    choice = int(input(f"[1]-> Manager bo'lib kirish\n[2]-> Foydalanuvchi bo'lib kirish\n[3]-> Chiqish\n"))
    if choice == 1:
        name =  input("Ismingizni kiriting: ")
        if name.upper() == management.ism.upper():
            while True:
                choice = int(input(f"[1]-> Samalyot qo'shish\n[2]-> Samalyotni olib tashlash\n[3]-> Uchuvchi qo'shish\n[4]-> Uchuvchini bo'shatish\n[5]-> Samalyotni uchishga tayorlash\n[6]-> Samalyotga yoqilg'i quyish\n[7]-> samalyotni uchirish\n[8]-> Asosiy oynaga qaytish\n"))

                if choice == 1:
                    plane = salamyot(input("Samalyot turi: "),int(input("Bak xajmini kiriting: ")),input("Samalyot uchish shaxrini kiriting: "),input("Samalyot qo'nadigan shaxarni kiriting: "),int(input("Samalyot o'rindiqlari sonini kiriting: "))) 
                    management.add_plane(plane)
                elif choice == 2:
                    if choice == 2:
                        if len(management.airport.planes) == 0:
                            print("Airportda hozirda birorta ham samalyot mavjud emas oldin samalyot qo'shing !\n")
                            plane = salamyot(input("Samalyot turi: "),int(input("Bak xajmini kiriting: ")),input("Samalyot uchish shaxrini kiriting: "),input("Samalyot qo'nadigan shaxarni kiriting: "),int(input("Samalyot o'rindiqlari sonini kiriting: "))) 
                            management.add_plane(plane)
                        else:
                            for i, plane in enumerate(management.airport.planes):
                                print(f"{i+1}. {plane.turi}")
                            plane_number = int(input("Qaysi raqam ostidagi samalyotni sotib yubormoqchisiz: ")) - 1

                            if plane_number < 0 or plane_number >= len(management.airport.planes):
                                print("Mavjud bo'lmagan raqam\n")
                            else:
                                removed_plane = management.airport.planes[plane_number]
                                management.remove_plane(removed_plane)
                                print(f"{removed_plane.turi} Samalyot airportdan chiqarildi \n")

                elif choice == 3:
                    pilot = uchuvchi(input("Uchuvchining ismi: "),int(input("Uchuvchining yoshi: ")))
                    management.add_employe(pilot)

                    print(f"Uchuvchi muofiqiyatli ishga olindi !")

                elif choice == 4:
                    if len(management.airport.employees) == 0:
                        print("Hozirda hech qanday ishchi mavjud emas oldin ichchi qo'shing !")
                        pilot = uchuvchi(input("Uchuvchining ismi: "),int(input("Uchuvchining yoshi: ")))
                        management.add_employe(pilot)
                    else:
                        for i, employee in enumerate(management.airport.employees):
                            print(f"{i+1}. {employee.ismi}")
                        employee_number = int(input("Qaysi raqam ostidagi uchuvchini bo'shatmoqchisiz: ")) - 1

                        if employee_number < 0 or employee_number >= len(management.airport.employees):
                            print("Mavjud bo'lmagan raqam")
                        else:
                            removed_employee = management.airport.employees[employee_number]
                            management.remove_employe(removed_employee)
                            print(f"{removed_employee.ismi} Airportdan bo'shatildi")

                elif choice == 5:
                    if len(management.airport.planes) == 0:
                        print("Tekshirish uchun samalyot mavjud emas oldin samalyot qo'shing !")
                        plane = salamyot(input("Samalyot turi: "),int(input("Bak xajmini kiriting: ")),input("Samalyot uchish shaxrini kiriting: "),input("Samalyot qo'nadigan shaxarni kiriting: "),int(input("Samalyot o'rindiqlari sonini kiriting: "))) 
                        management.add_plane(plane)

                    else:
                        for i, plane in enumerate(management.airport.planes):
                            print(f"{i+1}. {plane.turi}")
                        plane_number = int(input("Qaysi raqam ostidagi samalyotni tekshirmoqchisiz: ")) - 1

                        if plane_number < 0 or plane_number >= len(management.airport.planes):
                            print("Mavjud bo'lmagan raqam !")
                        else:
                            masofa = int(input(f"{management.airport.planes[plane_number].uchish_shaxri} dan {management.airport.planes[plane_number].qonish_shaxri} gacha necha km: "))
                            plane_to_check = management.airport.planes[plane_number]
                            if management.check_airplane(plane_to_check, masofa):
                                print(f"{plane_to_check.turi} Uchish uchun tayyor")
                            else:
                                print(f" {plane_to_check.turi} Uchish uchun tayyor emas")

                elif choice == 6:
                    if len(management.airport.planes) == 0:
                        print("Yoqilg'i to'ldirish uchun samalyot mavjud emas oldin samalyot qo'shing !")
                        plane = salamyot(input("Samalyot turi: "),int(input("Bak xajmini kiriting: ")),input("Samalyot uchish shaxrini kiriting: "),input("Samalyot qo'nadigan shaxarni kiriting: "),int(input("Samalyot o'rindiqlari sonini kiriting: "))) 
                        management.add_plane(plane)

                    else:
                        for i, plane in enumerate(management.airport.planes):
                            print(f"{i+1}. {plane.turi}")
                        plane_number = int(input("Qaysi raqam ostifagi samalyotga yoqilg'i to'ldirmoqchisiz: ")) - 1

                        if plane_number < 0 or plane_number >= len(management.airport.planes):
                            print("Mavjud bo'lmagan raqam !")
                        else:
                            plane_to_fill = management.airport.planes[plane_number]
                            management.fill_up(plane_to_fill)
                            print(f"{plane_to_fill.turi} yoqilg'i bilan to'ldirildi")

                if choice == 7:
                    if len(management.airport.planes) == 0:
                        print("Uchish uchun samalyot mavjud emas oldin samalyot qo'shing !")
                        plane = salamyot(input("Samalyot turi: "),int(input("Bak xajmini kiriting: ")),input("Samalyot uchish shaxrini kiriting: "),input("Samalyot qo'nadigan shaxarni kiriting: "),int(input("Samalyot o'rindiqlari sonini kiriting: "))) 
                        management.add_plane(plane)
                    elif len(management.airport.employees) == 0:
                        print("Uchuvchi mavjud emas oldin uchuvchi ishga olin !")
                        pilot = uchuvchi(input("Uchuvchining ismi: "),int(input("Uchuvchining yoshi: ")))
                        management.add_employe(pilot)
                    else:
                        for i, plane in enumerate(management.airport.planes):
                            print(f"{i+1}. {plane.turi}")
                        plane_number = int(input("Qaysi raqamdagi samaylotni uchirish kerak: ")) - 1

                        for i, employee in enumerate(management.airport.employees):
                            print(f"{i+1}. {employee.ismi}")
                        employee_number = int(input(f"Qaysi raqam ostidagi uchuvchi {management.airport.planes[plane_number].turi} ni boshqaradi: ")) - 1

                        if plane_number < 0 or plane_number >= len(management.airport.planes):
                            print("Mavjud bolmagan raqam")
                        elif employee_number < 0 or employee_number >= len(management.airport.employees):
                            print("mavjud bo'lmagan raqam")
                        else:
                            masofa = int(input(f"{management.airport.planes[plane_number].uchish_shaxri} dan {management.airport.planes[plane_number].qonish_shaxri} gacha necha km: "))
                            plane_to_launch = management.airport.planes[plane_number]
                            pilot_to_launch = management.airport.employees[employee_number]

                            pilot_to_launch.launch_airplane(plane_to_launch, masofa, management)

                elif choice == 8:
                    break
                else:
                    print("Mavjud bo'lmagan bo'lim !")
                    continue
        else:
            print("Bunday boshqaruvchi mavjud emas !")
            continue

    elif choice == 2:
        login = yolovchi(input("Ismingizni kiriting: "),int(input("Yoshingizni kiriting: ")),input("Xozirda yashaydigan joyingizni kiriting: "),input("Uchmoqchi bo'lgan shaxringizni kiriting: "),int(input("Qancha pulingiz bor: ")))
        login.book_flight(management)
    elif choice == 3:
        exit("Bugungi ish kuni tugadi !")
    else:
        print("Mavjud bo'lmagan bo'lim !")
        continue    