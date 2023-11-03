# Товарный ассортимент
assort=[
    ['Пельмени Сибирские',250],
    ['Равиоли',400],
    ['Пельмени Кирилловские',350],
    ['Пельмени с рыбой',150]
]

def check(assort):
    global full, sib, rav, kiril, fish
    for i in range(0, len(assort)):
        x=int(input(f'Сколько надо {assort[i][0]}: '))
        assort[i].append(x)
    sum=0 # Переменнная для накопления общей суммы покупки
    itog=0
    full=0
    sib=0
    rav=0
    kiril=0
    fish=0
    print('ООО "Русские пельмени"')
    print('======================')
    # Цикл, в котором будут выводиться название, кол-во и цена
    for pelmen in assort:
        name=pelmen[0]
        amount=pelmen[2]
        price=pelmen[1]
        print(f'{name} ({amount} шт.) - {price} руб.')
        if name=='Пельмени Сибирские':
            sib=sib+price*amount
        if name=='Равиоли':
            rav=rav+price*amount
        if name=='Пельмени Кирилловские':
            kiril=kiril+price*amount
        if name=='Пельмени с рыбой':
            fish=fish+price*amount
        sum=price*amount # Подсчёт общей суммы
        itog=itog+sum
        full=full+itog
        print(f'Итого: {sum} руб.')
        print('==================')
    print('________________________________')
    print(f'Сумма всей покупки: {itog} руб.')
    print('Спасибо за покупку')

print('Кассовая смена открыта! Удачной работы!')
i=0
p=0
while i!=1:
    quest=input('Вы хотите сделать новый чек или закрыть смену? (Чек/Закрыть смену): ')
    if quest=='Закрыть смену' and p==0:
        print('Вы не можете закрыть смену, т.к. вы её только открыли')
    if quest=='Чек' and p==1:
        check(assort)
    if quest=='Чек' and p==0:
        check(assort)
        p=p+1
    if quest not in ['Чек', 'Закрыть смену']:
        print('Неверный ввод. Пожалуйста, выберите вариант: Чек или Закрыть смену')
    if quest=='Закрыть смену' and p==1:
        print('Смена закрыта. Вот её результаты --->')
        print('Купленно Пельменей Сибрских на сумму', sib)
        print('Купленно Равиолей на сумму', rav)
        print('Купленно Пельменей Кирилловских на сумму', kiril)
        print('Купленно Пельменей с рыбой на сумму', fish)
        print('Выручка за сегодня составила', full,'руб.')
        i=1
    
