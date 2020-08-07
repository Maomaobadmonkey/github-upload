def get_percentage(num, round_digits=None):
    if round_digits is None:
        return str(round(num * 100)) + '%'
    else:
        rounding = round(num * 100, round_digits)
        return str(rounding) + '%'
