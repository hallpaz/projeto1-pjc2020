from datetime import date, datetime

# data = date(day= '27', month='10', year='2020')
# date.today
# print(data)
# print('Hoje', date.today())
# partes = '12/04/1994'.split('/')
# partes = [int(d) for d in partes]
# data = date(day=partes[0], month=partes[1], year=partes[2])
# idade_dias = date.today() - data

# print(int(idade_dias.days/365))
agora = datetime.now()
print(agora.date())
print(agora.time())