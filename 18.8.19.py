price = 0
tickets = int(input("Сколько билетов хотите преобрести:"))
for age in range(tickets):
    age = int(input("Возраст посетителя:"))
    if age < 18:
        price += 0
    elif 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390
print( "Кол-во билетов:", tickets, "шт." )
if tickets > 3 :
    sale = price / 100 * 10
    print("Цена без скидки:", price, "руб.")
    print("Скидка составляет:", int(sale), "руб.")
    print("К оплате с учетом скидки:", int((price - sale)), "руб.")
if tickets < 4 :
    no_sale = price
    print( "К оплате:", no_sale, "руб." )
