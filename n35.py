playlist = ["Warmup A", "Warmup B", "Hit X", "Hit Y"]
player = {"volume": 60, "mode": "normal", "speed": 1.0, "hour": 21}
scarga = False

def quiet_time(v = 60, m = 'normal', s = 1.0):
    player['volume'] = v
    player['mode'] = m
    player['speed'] = s


if player["hour"] >= 22:
    quiet_time(50, 'quiet', 1.0)
    scarga = True
elif player["hour"] >= 20:
    if player['volume'] <= 100:
        v = player['volume']
    else:
        v = 75

    quiet_time(v, 'party', 1.0)
else:
    quiet_time(75, 'quiet', 1.0)


if scarga == True:
    if player['mode'] == 'party':
        m = 'quiet'
    quiet_time(50, m, 1.0)