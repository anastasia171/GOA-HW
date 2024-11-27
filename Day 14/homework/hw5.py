#5) შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.

num = int(input("enter any number: "))

if num > 10 and num < 50:
    print("metia 10ze da naklebia 50ze")

elif num < 10 or num > 50:
    print("naklebia 10ze an metia 50")