#3) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი ცალკე და მხოლოდ კენტი რიცვხების ჯამი ცალკე, გამოიყენეთ for loop

user_number = int(input("enter num: "))

even_sum = 0
odd_sum = 0

for i in range (user_number):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print("even number sum => " + str(even_sum))
print("odd number sum => " + str(odd_sum))
