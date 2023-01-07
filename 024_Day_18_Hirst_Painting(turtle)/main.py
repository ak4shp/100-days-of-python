import colorgram

def get_image_colors(image:str) -> list:
    image_colors = colorgram.extract(image, 30)
    rgb_colors = []
    for color in image_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors

print(get_image_colors("image.jpg"))