#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop

number = int(input("enter number: "))

i = 0
for i in range(1, number + 1):
    if i % 2 == 0:
       i += i

print(i)