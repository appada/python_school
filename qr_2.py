import flet as ft
import qrcode
from io import BytesIO
from PIL import Image

def main(page: ft.Page):
    page.theme_mode='light'
    # QR 코드 생성 함수
    def generate_qr_code(e):
        qr_data = input_field.value
        if qr_data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

            # 이미지를 바이트로 변환
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            
            # Flet Image 컨트롤에 이미지를 설정
            qr_image.src = buffer.getvalue()
            page.update()

    # 입력 필드와 버튼 생성
    input_field = ft.TextField(label="Enter text for QR code:", width=300)
    generate_button = ft.ElevatedButton(text="Generate QR Code", on_click=generate_qr_code)

    # QR 코드를 표시할 이미지 컨트롤 생성
    qr_image = ft.Image(src='test')

    # 페이지에 컨트롤 추가
    page.add(input_field, generate_button, qr_image)

# Flet 앱 실행
ft.app(target=main)