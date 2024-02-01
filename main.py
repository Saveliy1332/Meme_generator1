from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text = input("Введи верхний текст: ")
bottom_text = input("Введи нижний текст: ")


print(top_text, bottom_text)

print("Список картинок: ")

print("1.Кот и две девушки")
print("2.Качок кот")

image_nummber = int(input("Введи номер картинки:"))


if image_nummber == 1:
  image_file = ("Мем кот и две девушки.jpg")
elif image_nummber == 2:
  image_file = ("Мем качок кот.jpg")

image = Image.open(image_file)

width, height = image.size

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arifal.ttf', size=70)

text = draw.textbbox((0, 0 ), top_text, font)
text_width = text[2]
draw.text(((width - text_width) / 2, 10), top_text, font=font, fill = 'black')

text = draw.textbbox ((0, 0),  bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill = 'black')
image.save("new_meme.jpg")