import colorama


def chardiff(a, b, marker=colorama.Style.BRIGHT):
    s = ""
    marked = False
    for i in range(len(a)):
        if i < len(b):
            if a[i] != b[i]:
                if not marked:
                    s += marker
            else:
                marked = False
                s += colorama.Style.RESET_ALL
        else:
            s += marker
        s += a[i]
    if marked:
        s += colorama.Style.RESET_ALL
    return s


def get_color(color):
    color = color.upper()
    if not hasattr(colorama.Fore, color):
        raise RuntimeError("Chosen color does not exist in pallet.")
    return getattr(colorama.Fore, color)
