def NULL_not_found(object: any) -> int:
    t = type(object)
    begin = ""
    if (object is None):
        print(f"Nothing: {object} {t}")
    elif (t == float and  object != object):
        print(f"Cheese: {object} {t}")
    elif (t == int and object == 0):
        print(f"Zero: {object} {t}")
    elif (t == str and not object):
        print(f"Empty: {t}")
    elif (t == bool and not object):
        print(f"Fake: {object} {t}")
    else:
        return 1
    return 0