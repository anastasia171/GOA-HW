# 1) გააკეთეთ სარეგისტრაციო, მომხმარებელს შემოატანიეთ სახელი და პაროლი, რეგისტრაციის შემდეგ მოხმარებელი უნდა შევიდეს ექაუნთზე, შეეკითხეთ სახელი და პაროლი მომხარებელს რათა შევიდეს ექაუნთზე სანამ მომხმარებელი არ შეიტანს იმ ინფორმაციას რაც შეიყვანა რეგისტრაციის დროს მანამ დაიბეჭდოს რომ შეტანილი ინფორმაცია არასწორია და შეეკითხოს თავიდან, ხოლო თუ მომხმარებელმა ყველაფერი სწორად შეიყვანა დაიბეჭდოს welcome

print("registration")
print()
name = input("enter username: ")
password = input("enter password: ")
print()
print("done")
print("sign in")
print()
name1 = input("enter your username: ")
password1 = input("enter your password: ")

if name == name1 and password == password1:
    print("welcome")
else:
    print("password or usename incorrect")