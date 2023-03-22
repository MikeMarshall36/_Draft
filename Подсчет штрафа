def speed_limit(speed: int, signals: list) -> int:
    fine = 0
    for i in range(len(signals)):
        if 10 <= speed - int(signals[i]) < 20:
            fine += 100
        if 20 <= speed - int(signals[i]) < 30:
            fine += 250
        if 30 <= speed - int(signals[i]):
            fine += 500
    else:
        return fine


print(speed_limit(100, [110, 100, 80]))
