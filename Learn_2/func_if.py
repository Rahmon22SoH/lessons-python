temperature = int(input("Ввидите температуру "))
def check_wacher (temperature):
    if temperature <= 0:
        return "На улице холодно "
    elif temperature >= 8:
        return "На улице прохладно"
    elif temperature >= 20:
        return "На улице тепло"
    elif temperature >= 30:
        return "На улице жарко"
    return 'Не работает'


print(check_wacher(temperature)) # "На улице холодно"

temperature = int(input("Ввидите температуру "))
def check_wacher (temperature):
    if temperature <= 0:
        return "На улице холодно "
    elif temperature >= 0 and temperature <= 15:
        return "На улице прохладно"
    elif temperature >= 15 and temperature <= 25:
        return "На улице тепло"
    else:
        return "На улице жарко"
    return 'Не работает'
