from PIL import Image

im = Image.open('icon_entering_two@3x.png')
w, h = im.size
print('Original image size: %s%s' % (w, h))

im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

im.save('thumbnail.png', 'PNG')

