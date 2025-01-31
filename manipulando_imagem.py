from PIL import Image

imagem = Image.open("flor.jpg")

blackAndWhite = imagem.convert('L')
blackAndWhite.save('bw_flor.jpg')
blackAndWhite.show()
