import re
import random
import colorsys


MAX_RGB = 255
MAX_HUE = 360
MAX_LIGHTNESS = 100
MAX_SATURATION = 100
    
REGEX = r'hsl\(\s*(\d+),\s*(\d+)%,\s*(\d+)%\s*\)'

RED = (0, 100, 40)
BLUE = (225, 100, 40)
BROWN = (29, 100, 30)
GREEN = (120, 100, 36)
YELLOW = (50, 100, 45)


def get_hex(hsl):
    return get_hsl_to_hex(*hsl)


def get_color_with_random_lightness(hsl):
    delta = 20
    h, s, l = hsl

    d = random.randint(0, delta)
    l = (l+d) if (random.randint(0, 10) > 8) else (l-d)

    return get_hsl_to_hex(h, s, l)


def random_color_in_list(color_list):
    color = random.choice(color_list)
    return get_color_with_random_lightness(color)


def get_hsl_to_hex(h, s, l):
    color = f"hsl({h}, {s}%, {l}%)"
    return convert_hsl_to_hex(color)


def convert_hsl_to_hex(hsl):
    color = re.findall(REGEX,hsl)[0]
    
    rgb = colorsys.hls_to_rgb(
        int(color[0])/MAX_HUE, 
        int(color[2])/MAX_SATURATION, 
        int(color[1])/MAX_LIGHTNESS
    )

    hex = '#%02x%02x%02x'%(
        round(rgb[0]*MAX_RGB),
        round(rgb[1]*MAX_RGB),
        round(rgb[2]*MAX_RGB)
    )
    return hex


if __name__ == '__main__':
    hsl = (20, 80, 20)

    color = get_hsl_to_hex(*hsl)
    color = get_color_with_random_lightness(hsl)
    print(color)

    hsl = (10, 20, 20)
    c = get_hex(hsl)
    print(c)