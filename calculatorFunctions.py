SMOKE_VALUE = 2.725
WEED_VALUE = 60

def calculate(smokes, weed):
    value = 0.0
    value += smokes * SMOKE_VALUE
    value += weed * WEED_VALUE
    return value