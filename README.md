# Manipulando imagem

Script em Python que converte uma imagem colorida para escala de cinza (preto e branco), usando a biblioteca Pillow.

## Tecnologias

- Python
- [Pillow](https://pypi.org/project/Pillow/) (PIL) — biblioteca para processamento de imagens

## Como funciona

1. Abre uma imagem colorida (`flor.jpg`)
2. Converte para escala de cinza com `.convert('L')`
3. Salva o resultado em um novo arquivo (`bw_flor.jpg`)
4. Exibe a imagem convertida na tela

## Como rodar

```bash
pip install Pillow
python manipulando_imagem.py
```
