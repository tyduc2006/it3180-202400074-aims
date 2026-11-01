def search_by_title(cart, title):
    result = []

    for dvd in cart.items:
        if title.lower() in dvd.title.lower():
            result.append(dvd)

    return result


def search_by_name(cart, name):
    result = []

    for dvd in cart.items:
        if name in dvd.title:
            result.append(dvd)

    return result
