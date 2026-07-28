from PIL import Image

img = Image.open("logo.png").convert("RGBA")
pixels = list(img.getdata())

new_pixels = []

for r, g, b, a in pixels:
    # البكسل يعتبر خلفية بيضاء إذا كانت قيم R,G,B كلها عالية جداً ومتقاربة
    is_white = r > 245 and g > 245 and b > 245
    if is_white:
        new_pixels.append((r, g, b, 0))   # شفاف تماماً
    else:
        new_pixels.append((r, g, b, a))   # بدون تغيير

img.putdata(new_pixels)
img.save("logo_transparent.png")
print("Done! logo_transparent.png saved.")
