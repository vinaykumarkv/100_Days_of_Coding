import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('painting.jpg', 30)

def rgbcolor():
    rgbcolors = []
    for i in colors:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        newtuple = (r, g, b)
        rgbcolors.append(newtuple)
    return rgbcolors
c = rgbcolor()
print(c)