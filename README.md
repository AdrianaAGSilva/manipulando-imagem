# Manipulando imagem

Script em Python que converte uma imagem colorida para escala de cinza (preto e branco), usando a biblioteca Pillow.

## Tecnologias

- Python
- [Pillow](https://pypi.org/project/Pillow/) (PIL) — biblioteca para processamento de imagens

## Como funciona

1. Abre uma imagem colorida
2. Converte para escala de cinza com `.convert('L')`
3. Salva o resultado em um novo arquivo
4. Exibe a imagem convertida na tela

## Como rodar

```bash
pip install Pillow
python manipulando_imagem.py
```

> **Nota:** este projeto não inclui uma imagem de exemplo. Antes de rodar, substitua `"flor.jpg"` no código pelo caminho de uma imagem sua (ex: `"minha_foto.jpg"`), colocando o arquivo na mesma pasta do script.
