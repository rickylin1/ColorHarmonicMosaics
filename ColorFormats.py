# hexadecimal is base 16 
# we use the following formula
#rgb ranges from (0,255) where (0,0,0) is black and (255,255,255) is white
# R/16 = x + y/16
# G/16 = x' + y'/16
# B/16 = x" + y"/16
#where x is a whole number and y is the remainder of the respective rgb value divided by 16
#then we can represent a hexadecimal such as 50068F which has 6 digits
#the numbers go from 0 - 9, then A - F for 10 - 15 

hex_colors_string = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                  '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                  'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_colors = { 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    
def rgb_to_hex(r, g, b):
    r1, r2= r//16, int((r/16 - r//16) * 16)
    g1, g2= g//16, int((g/16 - g//16) * 16)
    b1, b2= b//16, int((b/16 - b//16) * 16)

    r1 = hex_colors[r1]
    g1 = hex_colors[g1]
    b1 = hex_colors[b1]
    r2 = hex_colors[r2]
    g2 = hex_colors[g2]
    b2 = hex_colors[b2]
   

    hex = str(r1) + str(r2) + str(g1) + str(g2) + str(b1) + str(b2)
    return hex

def hex_to_rgb(hex):
    l, r = 0, 1
    rgb = []
    for i in range(3):
        convert = hex_colors_string[hex[l]] * 16 + hex_colors_string[hex[r]]
        rgb.append(convert)
        l += 2
        r += 2
    return rgb

def rgb_to_cymk(r,g,b):
    white = max(r/255, g/255,b/255)
    cyan = (white - (r/255))/white
    magenta = (white - (g/255))/white
    yellow = (white - (b/255))/white
    black = 1 - white


def complementary_rgb_255(r, g, b):
    cr = 255 - r
    cg = 255 - g
    cb = 255 - b
    print(cr,cg,cb)
    return cr, cg, cb

complementary_rgb_255(255,192,203)


