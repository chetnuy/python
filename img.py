from PIL import Image, ImageDraw, ImageGrab
#смотрим версию
#print(Image.VERSION)
'''
# позволяет переконвертировать изображение и сжать
foto = Image.open("png.png")
foto.load()
print(foto.getpixel((25,45)))
foto.putpixel((25,25), (255, 0, 0))

print(foto.getpixel((25,45)))
foto.show() " открываем файл для просмотра
foto.save('tmp.jpg')
'''
'''
# смотрим разрешение файла и формат
file = Image.open('tmp.jpg')
print(file.format)
print(file.size)
'''
#foto = Image.open('png.png')
#foto.save('qual.jpg','JPEG', quality=100 ) #задаем качество изображения


# создаем новое изображение
#img = Image.new('RGB', (700,700), 'green')
#img.show()
'''

img = Image.open('png.png')
#print(img.size, img.mode, img.format, img.info) # выводим информацию по изображению
dmg2 = img.copy()
dmg2.show() # создаем копию и затем открываем его
'''

'''
# меняем разрешение изображения
# для сохранения копии нужно использовать resize вместо thumbnail
img = Image.open('png.png')
img.thumbnail((600,400), Image.LANCZOS)
print(img.size)
img.show()

'''
'''
# Поворачиваем изображение
img = Image.open('png.png')
#img.thumbnail((600,400), Image.LANCZOS)
img2 = img.rotate(90, expand=True)
print(img.size)
img2.show()
'''

'''
# зеркалируем изображение
# а также возможно вырезать всталять объекты изображение
img = Image.open('png.png')
img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.show()
'''
'''
# рисуем на изображении
img = Image.new("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)
for n in range(5, 31):
    draw.point( (n, 5), fill=(255, 0, 0) )
img.show()
'''

# # работает на винде или на маке
# img = ImageGrab.grab()
# img.save('scren.bmp', 'BMP')
# img.show()
# img.mode

