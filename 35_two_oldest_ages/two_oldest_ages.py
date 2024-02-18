def two_oldest_ages(ages):
    un_age = set(ages)
    oldest = sorted(un_age)[-2:]
    return tuple(oldest)