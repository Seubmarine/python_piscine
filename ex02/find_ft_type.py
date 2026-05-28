def all_thing_is_obj(object: any) -> int:
    t = type(object)
    name = t.__name__.capitalize()
    
    if (t is str):
        print(f"{object} is in the kitchen : {t}")
    elif (t is int):
        print("Type not found")
    else:
        print(f"{name} : {t}")
    return 42