import qrcode
import qrcode.image.svg
from qrcode.image.pil import PilImage

from utils import validate_input


def main():
    print("*" * 38)
    print(("*" * 10) + " QRCODE GENERATOR " + ("*" * 10))
    print("*" * 38)

    nom_image = ""
    url = ""
    size = 10
    color = (0, 0, 0)

    format_input = ""
    color_input = ""

    inputs_validated = False
    while not inputs_validated:
        url = input("Url (obligatoire) : ").strip()
        nom_image = input("Nom de l'image (par défaut : qrcode) : ").strip()
        size_input = input("Taille du QRcode (valeur par défaut 10 : 10 x 33 = 330px): min=1 max=100 : ").strip()
        color_input = input("Couleur RGB (laissez vide pour la couleur par défaut : Noir ) Format: 55,95,35 : ").strip()
        format_input = input("Format du QRcode (Laissez vide pour la valeur par défaut PNG), Dispo : SVG : ").strip()

        inputs_validated = validate_input([
            ('url', url),
            ('size_input', size_input)
        ])

        if inputs_validated:
            if size_input.isnumeric():
                size = size_input

    if len(color_input) > 0:
        color = tuple(map(int, color_input.split(',')))

    qr_code_generator(name=nom_image, url=url, size=size, color=color, format_=format_input)


def qr_code_generator(name="", url=None, size=10, color=(0, 0, 0), format_=None):
    # Creating an instance of qrcode
    """
        box_size = 33px * number
    """

    if format_ == 'SVG':
        format_image = qrcode.image.svg.SvgPathImage
    else:
        format_image = PilImage
        format_ = 'png'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=2,
        image_factory=format_image
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color='white')

    if len(name) == 0:
        name = f"qrcode.{format_.lower()}"
    else:
        name = f"{name}.{format_.lower()}"

    img.save(name)


if __name__ == '__main__':
    main()
