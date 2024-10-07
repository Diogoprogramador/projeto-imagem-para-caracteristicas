from PIL import Image

# Mapeamento de caracteres para diferentes níveis de brilho
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Função para redimensionar a imagem, mantendo a proporção
def redimensionar_imagem(img, nova_largura=100):
    largura, altura = img.size
    proporcao = altura / largura / 1.65  # Ajuste para manter proporção correta
    nova_altura = int(nova_largura * proporcao)
    img = img.resize((nova_largura, nova_altura))
    return img

# Função para converter imagem para escala de cinza
def converter_para_cinza(img):
    return img.convert("L")

# Função para mapear pixels em caracteres ASCII
def pixel_para_ascii(pixel):
    return ASCII_CHARS[pixel // 25]  # Dividir por 25 para mapear em 11 níveis de brilho

# Função para converter a imagem em arte ASCII
def imagem_para_ascii(caminho_imagem, nova_largura=100):
    # Abrir imagem
    try:
        img = Image.open(caminho_imagem)
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return

    # Redimensionar e converter para cinza
    img = redimensionar_imagem(img, nova_largura)
    img = converter_para_cinza(img)

    # Converter pixels para caracteres ASCII
    pixels = img.getdata()
    ascii_str = "".join([pixel_para_ascii(pixel) for pixel in pixels])

    # Organizar o texto em linhas de acordo com a largura da imagem
    largura = img.width
    ascii_imagem = [ascii_str[i:i + largura] for i in range(0, len(ascii_str), largura)]
    return "\n".join(ascii_imagem)

# Caminho da imagem PNG
caminho_imagem = 'vasco.png'  # Substitua pelo caminho da sua imagem

# Converter e imprimir a arte ASCII
arte_ascii = imagem_para_ascii(caminho_imagem)

if arte_ascii:
    print(arte_ascii)
