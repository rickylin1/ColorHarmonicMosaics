from PIL import Image
import os

def create_single_color_image(color, size=(150, 150), filename='single_color_image.png'):
    """
    Create an image of a single color.

    Parameters:
    - color: tuple of RGB (e.g., (255, 0, 0)) or hex (e.g., "#FF0000") color code.
    - size: tuple of width and height (default is 150x150).
    - filename: name of the file to save the image (default is 'single_color_image.png').

    Returns:
    - None
    """
    # Convert hex color to RGB if needed
    if isinstance(color, str):
        if color.startswith('#'):
            color = color.lstrip('#')
            color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    
    # Create an image
    image = Image.new("RGB", size, color)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Save the image
    image.save(filename)
    print(f"Image saved as {filename}")



def rainbow():
    # Create a folder called 'folder' and save images inside it
    folder = 'rainbow'

    create_single_color_image((255, 0, 0), size=(150, 150), filename=f'{folder}/red_image.png')
    create_single_color_image((255, 165, 0), size=(150, 150), filename=f'{folder}/orange_image.png')
    create_single_color_image((255, 255, 0), size=(150, 150), filename=f'{folder}/yellow_image.png')
    create_single_color_image((0, 255, 0), size=(150, 150), filename=f'{folder}/green_image.png')
    create_single_color_image((0, 0, 255), size=(150, 150), filename=f'{folder}/blue_image.png')
    create_single_color_image((75, 0, 130), size=(150, 150), filename=f'{folder}/indigo_image.png')
    create_single_color_image((238, 130, 238), size=(150, 150), filename=f'{folder}/violet_image.png')

def add_tint(color, factor):
    """
    Add a tint to the given color by blending it with white.
    :param color: Tuple of (R, G, B) values.
    :param factor: Float in range [0, 1] where 0 is the original color and 1 is white.
    :return: Tuple of (R, G, B) values for the tinted color.
    """
    r, g, b = color
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return (r, g, b)

def add_shade(color, factor):
    """
    Add a shade to the given color by blending it with black.
    :param color: Tuple of (R, G, B) values.
    :param factor: Float in range [0, 1] where 0 is the original color and 1 is black.
    :return: Tuple of (R, G, B) values for the shaded color.
    """
    r, g, b = color
    r = int(r * (1 - factor))
    g = int(g * (1 - factor))
    b = int(b * (1 - factor))
    return (r, g, b)

def generate_monochrome_scheme(color, num_tints=20, num_shades=20):
    """
    Generate a monochrome color scheme with tints and shades.
    :param color: Tuple of (R, G, B) values.
    :param num_tints: Number of tints to generate.
    :param num_shades: Number of shades to generate.
    :return: List of (R, G, B) values for the color scheme.
    """
    scheme = [color]
    for i in range(1, num_tints + 1):
        scheme.append(add_tint(color, i / (num_tints + 1)))
    for i in range(1, num_shades + 1):
        scheme.append(add_shade(color, i / (num_shades + 1)))
    return scheme

# Example usage:
# original_color = (100, 150, 200)  # Example RGB color
# original_color = (255,0,0)
# monochrome_scheme = generate_monochrome_scheme(original_color)
# counter = 1
# for color in monochrome_scheme:
#     print(color)
    # folder = 'monochrome'
    # create_single_color_image(color, size=(150, 150), filename=f'{folder}/{counter}.png')
    # counter+=1

#NOTE this complementary is for the rgb model, which means these are complementary colors 
# Red and Cyan
# Green and Magenta
# Blue and Yellow

# instead of the rgb complementary colors
# Red and Green
# Yellow and Purple
# Blue and Orange

def find_complementary_color(rgb_color):
    """
    Find the complementary color of the given RGB color.
    :param rgb_color: Tuple of (R, G, B) values.
    :return: Tuple of (R, G, B) values for the complementary color.
    """
    r, g, b = rgb_color
    complementary_color = (255 - r, 255 - g, 255 - b)
    return complementary_color

# Example usage:
# rgb_color = (255,0,0)  # Example RGB color
# complementary_color = find_complementary_color(rgb_color)
# print("Original RGB color:", rgb_color)
# print("Complementary RGB color:", complementary_color)

def find_analogous_colors(rgb_color, num_colors=3, angle=30):
    """
    Find analogous colors for the given RGB color.
    :param rgb_color: Tuple of (R, G, B) values.
    :param num_colors: Number of analogous colors to generate (including the original color).
    :param angle: Angle (in degrees) to determine how far apart the analogous colors should be on the color wheel.
    :return: List of tuples, each tuple represents an analogous RGB color.
    """
    r, g, b = rgb_color
    analogous_colors = []
    for i in range(num_colors):
        hue_shift = angle * (i - (num_colors // 2))
        h, s, v = rgb_to_hsv(r, g, b)
        new_h = (h + hue_shift) % 360
        new_r, new_g, new_b = hsv_to_rgb(new_h, s, v)
        analogous_colors.append((new_r, new_g, new_b))
    return analogous_colors

def rgb_to_hsv(r, g, b):
    """
    Convert RGB to HSV (Hue, Saturation, Value/Brightness).
    :param r: Red value (0-255).
    :param g: Green value (0-255).
    :param b: Blue value (0-255).
    :return: Tuple of (H, S, V) where H is in range [0, 360], S and V are in range [0, 1].
    """
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    delta = max_rgb - min_rgb

    v = max_rgb / 255.0

    if max_rgb != 0:
        s = delta / max_rgb
    else:
        s = 0

    if delta == 0:
        h = 0
    elif r == max_rgb:
        h = (g - b) / delta
    elif g == max_rgb:
        h = 2 + (b - r) / delta
    else:
        h = 4 + (r - g) / delta

    h *= 60
    if h < 0:
        h += 360

    return h, s, v

def hsv_to_rgb(h, s, v):
    """
    Convert HSV (Hue, Saturation, Value/Brightness) to RGB.
    :param h: Hue value in degrees (0-360).
    :param s: Saturation value (0-1).
    :param v: Value/Brightness value (0-1).
    :return: Tuple of (R, G, B) where each value is in range [0, 255].
    """
    h /= 60
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))

    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q

    return int(r * 255), int(g * 255), int(b * 255)

# Example usage:
# rgb_color = (100, 150, 200)  # Example RGB color
# analogous_colors = find_analogous_colors(rgb_color)
# print("Original RGB color:", rgb_color)
# print("Analogous RGB colors:", analogous_colors)

def find_triadic_colors(rgb_color):
    """
    Find triadic colors for the given RGB color.
    :param rgb_color: Tuple of (R, G, B) values.
    :return: List of tuples, each tuple represents a triadic RGB color.
    """
    r, g, b = rgb_color
    triadic_colors = []

    # Calculate first triadic color (120 degrees apart)
    h1, s1, v1 = rgb_to_hsv(r, g, b)
    new_h1 = (h1 + 120) % 360
    new_r1, new_g1, new_b1 = hsv_to_rgb(new_h1, s1, v1)
    triadic_colors.append((new_r1, new_g1, new_b1))

    # Calculate second triadic color (240 degrees apart)
    h2, s2, v2 = rgb_to_hsv(r, g, b)
    new_h2 = (h2 + 240) % 360
    new_r2, new_g2, new_b2 = hsv_to_rgb(new_h2, s2, v2)
    triadic_colors.append((new_r2, new_g2, new_b2))

    return triadic_colors

# RGB to HSV and HSV to RGB functions as defined in the previous function

# Example usage:
# rgb_color = (100, 150, 200)  # Example RGB color
# triadic_colors = find_triadic_colors(rgb_color)
# print("Original RGB color:", rgb_color)
# print("Triadic RGB colors:", triadic_colors)

def is_warm_color(rgb_color):
    """
    Check if the given RGB color is a warm color.
    :param rgb_color: Tuple of (R, G, B) values.
    :return: True if the color is warm, False if it is cool.
    """
    r, g, b = rgb_color
    # Calculate a "warmth score" based on RGB values
    warmth_score = r - (g + b) / 2

    # Define a threshold to classify as warm or cool
    threshold = 20

    # Check if warmth score is above the threshold
    return warmth_score >= threshold

def is_cool_color(rgb_color):
    """
    Check if the given RGB color is a cool color.
    :param rgb_color: Tuple of (R, G, B) values.
    :return: True if the color is cool, False if it is warm.
    """
    return not is_warm_color(rgb_color)

# Example usage:
rgb_color_warm = (255, 165, 0)  # Example warm RGB color (orange)
rgb_color_cool = (0, 0, 255)    # Example cool RGB color (blue)

print("RGB color (255, 165, 0) is warm:", is_warm_color(rgb_color_warm))
print("RGB color (255, 165, 0) is cool:", is_cool_color(rgb_color_warm))
print("RGB color (0, 0, 255) is warm:", is_warm_color(rgb_color_cool))
print("RGB color (0, 0, 255) is cool:", is_cool_color(rgb_color_cool))

