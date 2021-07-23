# cars = ["toyota", 'mazda','hyundayi','gm','kia']
# for car in cars:
#     if car.lower() != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
#--------------------------------------------------------------------------------------------
# ism = input("Ismingiz nima? ")
# if ism.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {ism.title()}")
#--------------------------------------------------------------------------------------------
# print("Ikkita son kiriting:")
# a = float(input("a = "))
# b = float(input("b = "))
# if a == b:
#     print("Sonlar teng.")
#--------------------------------------------------------------------------------------------
# son = float(input("Istalgan son kiriting: "))
# if son > 0:
#     print(f"{son} ni musbat son")
# elif son < 0:
#     print(f"{son} ni manfiy son")

#--------------------------------------------------------------------------------------------
# son = float(input("Istalgan son kiriting: "))
# if son > 0:
#     print(son**(1/2))
# elif son < 0:
#     print('Musbat son kriting.')
#--------------------------------------------------------------------------------------------
# Chipta narxi 

# f_yoshi = int(input("Yoshingiz nechchida: "))
# if f_yoshi < 4 or f_yoshi > 60:
#     print("Sizga muzeyga kirish bepul. ")
# elif f_yoshi < 18:
#     print("Sizga kirish 10000 so'm.")
# else:
#     print("Sizag kirish 20.000 so'm")
#--------------------------------------------------------------------------------------------
# maxsulotlar  = ['un', 'yog','gush','non','tuz','shakar','olma','nok','guruch','mosh']
# savat = []
# bor_maxsulotlar = []
# mavjud_emas = []
# for maxsulot in range(5):
#     savat.append(input(f"Savatga {maxsulot+1}-axsulotni  qo'shing: "))
#     if savat[maxsulot] in maxsulotlar:
#         bor_maxsulotlar.append(savat[maxsulot])
#     else:
#         mavjud_emas.append(savat[maxsulot])
# if mavjud_emas:
#     for maxsulot in savat:
#         if maxsulot in maxsulotlar:
#             print(f"Do'konimizda {maxsulot} bor")
#         else:
#             print(f"Do'konimizda {maxsulot} yo'q")
# else:
#     print("Siz so'ragan barcha maxsulotlar do'konimizda mavjud.")

#----------------------------------------------------------------------------
# foydalanuvchilar = ['zokir','admin','botir','shokir','zorro']
# yangi_login = input("Yangi login tanlang: ")
# if yangi_login in foydalanuvchilar:
#     print("Login band, yangi login tanlang! ")
# else:
#     print(f"Xush kelibsiz {yangi_login.title()}")
#--------------------------------------------------------------------------------------------
butun_son = int(input("Biror butun sonni kiriting: "))
for son in range(2,11):
    if butun_son % son == 0:
        print(f"{butun_son} soni {son} ga qoldiqsiz bo'linadi.")