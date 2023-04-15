def sea_level_rise_calculator():
    start_sea_level = float(input("Введите начальный уровень моря: "))
    global_warming = float(input("Введите предполагаемое значение глобального потепления: "))
    sea_level_rise = (global_warming / 2.0) * start_sea_level
    print("При глобальном потеплении на", global_warming, "градусов, уровень моря поднимется на", sea_level_rise, "метров.")
    
sea_level_rise_calculator()
