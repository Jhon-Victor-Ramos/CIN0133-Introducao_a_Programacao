"""
    3h por dia
    12000 ticks que Tantan passou construindo (ciclo diurno, 10min na vida real)

"""


real_life_days = int(input())
houses_amount = int(input())

total_ticks_in_hours = 12000 * 3 # como 12000 são 10min, então multiplica por 6 para pegar quantos ticks jogáveis ele passou em uma hora

total_time_in_hours = real_life_days * 3

total_ticks_played = total_time_in_hours * total_ticks_in_hours

total_ticks_per_house = total_ticks_played // houses_amount

print(total_ticks_per_house)