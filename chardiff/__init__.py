import colorama


def chardiff(a, b, marker=colorama.Style.BRIGHT):
    s = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            s += marker
        s += a[i]
        s += colorama.Style.RESET_ALL
    return s


def get_color(color):
    color = color.upper()
    if not hasattr(colorama.Fore, color):
        raise RuntimeError("Chosen color does not exist in pallet.")
    return getattr(colorama.Fore, color)
