#3) შეამოწმეთ, არის თუ არა მოცემული ციფრი დადებითი ან ნული, თუმცა არ არის უარყოფითი.

num = int(input("enter number: "))

if num < 0:
    print("uaryofitia")

elif num > 0:
    print("dadebitia")