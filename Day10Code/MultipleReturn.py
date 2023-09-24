def format_name(name):
    if name == "":
        return f"Name '{name}' is not valid, please enter correct name."
    else:
        pass
    
    n = name.title()
    return n

    

name = "Geeta alam"
name = format_name(name)
print(name)

