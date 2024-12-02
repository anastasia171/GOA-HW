# 5) დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. თუ 10 დან 20 კილომდე ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში, თუ 30-40 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი ტაბლეტი უნდა დალიო ორჯერ დღეში. თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

weight = int(input("enter your weight: "))

if 10<= weight <=20:
    print("naxevari tableti unda dalio dgeshi")
elif 30>= weight <=40:
    print("erti tableti orjer dgeshi")
elif weight > 45:
    print("3 tableti orjer dgeshi")
else: 
    weight = int(input("enter your weight: "))