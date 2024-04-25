import datetime

#Время доставки должно назначаться как минимум на полтора часа позже нынешнего времени
def check_delivery(delivery):
    time = datetime.datetime.now() + datetime.timedelta(hours=1.5)
    if delivery.date >= time:
        print('Доставка оформлена')
        return True
    else:
        print('Доставка не может быть оформлена на данное время')
        return False
    
#Цветы не могут находится в магазине больше двух дней
def check_flowers(flowers):
    time = datetime.datetime.now() + datetime.timedelta(days=2)
    if flowers.date < time:
        print('Цветы можно продавать')
        return True
    else:
        print('Цветы надо утилизировать')
        return False

#Один курьер не может доставлять несколько букетов на одно и то же время
def check_time_delivery(deliveries, delivery):
    for d in deliveries:
        if delivery.time == d.time and delivery.id == d.id:
            print('Данный курьер занят в это время')
            return False
    return True

#Если прошел 1 день с момента поступления цветов, продаваить их со скидкой 20%
def check_time_flowers(flowers):
    check = False
    for flower in flowers:
        if datetime.datetime.now() >= (flower.date + datetime.timedelta(days=1)):
            flower.unitPrice = flower.unitPrice * 0.8
            check = True
    return check
    