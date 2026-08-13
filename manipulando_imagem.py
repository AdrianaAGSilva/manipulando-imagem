from PIL import Image

imagem = Image.open("flor.jpg")

preto_e_branco = imagem.convert('L')
preto_e_branco.save('bw_flor.jpg')
preto_e_branco.show()
