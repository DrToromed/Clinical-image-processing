from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps, ImageFont


def rx_info(rx_image):
    return f"Format: {rx_image.format}, Size: {rx_image.size}, Mode: {rx_image.mode}"


def rx_enhance(rx_image):
    rx_grises = rx_image.convert("L")
    rx_contrast = ImageOps.autocontrast(rx_grises)
    rx_contrast.save("rx_contrast.png")
    return rx_contrast


def rx_equalize(rx_image):
    rx_equalized = ImageOps.equalize(rx_image)
    rx_equalized.save("rx_image_equalized.png")
    return rx_equalized


def rx_shaper(rx_image):
    rx_sharped = rx_image.filter(ImageFilter.SHARPEN)
    rx_sharped.save("rx_sharper.png")
    return rx_sharped


def show_rx_comparativa(rx_img, img_en, img_eq, img_sh):
    ancho, alto = rx_img.size
    # Creamos el lienzo para las 4 imágenes
    lienzo = Image.new("L", (ancho * 4, alto))

    # Aseguramos que la original esté en escala de grises para el lienzo
    rx_img_l = rx_img.convert("L")

    # Pegamos cada versión
    lienzo.paste(rx_img_l, (0, 0))
    lienzo.paste(img_en, (ancho, 0))
    lienzo.paste(img_eq, (ancho * 2, 0))
    lienzo.paste(img_sh, (ancho * 3, 0))

    # --- DIBUJAR NOMBRES ---
    draw = ImageDraw.Draw(lienzo)
    etiquetas = ["1. ORIGINAL", "2. CONTRASTE", "3. ECUALIZADA", "4. NITIDEZ"]

    # CALCULAMOS EL TAMAÑO DE LETRA SEGÚN LA IMAGEN (5% del alto)
    # Esto evita que las letras se vean diminutas en RX grandes
    fnt_size = int(alto * 0.05)

    try:
        # Intentamos cargar Arial (estándar en Windows)
        fuente = ImageFont.truetype("arial.ttf", fnt_size)
    except:
        # Si falla, usamos la de reserva con un tamaño fijo grande
        fuente = ImageFont.load_default()

    for i, texto in enumerate(etiquetas):
        # Dibujamos un pequeño fondo negro para que el texto resalte (opcional)
        draw.rectangle([i * ancho + 10, 10, i * ancho + (fnt_size * 8), 10 + (fnt_size * 1.5)], fill=0)
        # Escribimos el nombre
        draw.text((i * ancho + 20, 20), texto, fill=255, font=fuente)

    lienzo.show()
    lienzo.save("comparativa_completa.png")


# --- FLUJO PRINCIPAL ---
rx_name = input("Introduce el nombre de tu Radiografía (ej: imagen.jpg): ")
try:
    rx_img = Image.open(rx_name)
    print(rx_info(rx_img))

    # Procesamiento en cadena
    img_en = rx_enhance(rx_img)
    img_eq = rx_equalize(img_en)
    img_sh = rx_shaper(img_eq)

    # Generar panel
    show_rx_comparativa(rx_img, img_en, img_eq, img_sh)

    print("¡Procesamiento completado con éxito!")
except FileNotFoundError:
    print("Error: No se encontró el archivo. Revisa el nombre y la extensión.")

