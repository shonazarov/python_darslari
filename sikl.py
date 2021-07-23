# ismlar = ['Botir','Bobir','Zokir','Shokir','qodir']
# s = 0
# for ism in ismlar:
#     s+=1
#     print(f"Salom {ism.title()}")
# print(f"Kod {s} marta takrorlandi")
# toq_sonlar = []
# for toq_s in range(10,100):
#     if toq_s%2!=0:
#         toq_sonlar.append(toq_s)
# for s in toq_sonlar:
#     print(s**3)


# kinolar = []
# for kino in range(0,5):
#     kinolar.append(input(f"{kino+1}-sevimli kinoyingiz nomini kiriting: "))
# print(kinolar)

suxbatdoshlar = []
k = int(input("Bugun nechta odam bilan suxbat qurdingiz? "))
for ism in range(0,k):
    suxbatdoshlar.append(input(f"{ism+1}-suhbat qilgan odamingiz kim edi: "))
print(suxbatdoshlar)