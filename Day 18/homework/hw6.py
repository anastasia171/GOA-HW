# 6)  დაბეჭდეთ ნულიდან 70 მდე რიცხვები ლუწ რიცხვებს გვერძე მიუწერეთ რომ ლუწია ხოლო კენტებს მიუწერეთ რომ კენტია

for i in range (70):
    if i % 2 == 0:
        print("luwia " + str(i))
    elif i % 2 == 1:
        print("kentia " + str(i))
    else: 
        print("error")