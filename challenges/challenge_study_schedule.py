def study_schedule(permanence_period, target_time):
    contador = 0
    for start, end in permanence_period:
        try:
            if start <= target_time <= end:
                contador += 1
        except TypeError:
            return None
    return contador
