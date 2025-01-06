# 1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი

num = int(input("enter number: "))

for i in range(num):
    num += i

print(num)