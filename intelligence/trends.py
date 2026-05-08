from collections import defaultdict

trend_state = defaultdict(list)


def add_snapshot(wallet, value):
    trend_state[wallet].append(value)


def is_accumulating(wallet):
    data = trend_state[wallet]

    if len(data) < 3:
        return False

    return data[-1] > data[-2] > data[-3]