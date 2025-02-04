import os
import flet as ft
import qrcode
import base64
import io


from datetime import datetime

def main(page: ft.Page):
     page.window.height = 500
     page.window.width = 500
     page.title = 'QR code'

     #def get_img_path(filename='qrcode.jpg'):
     #   """Return the absolute path for the QR code image."""
       # current_dir = Path.cwd() # from pathlib import Path
     #   return current_dir / filename

     def create_qr(e):
         if not input_text.value:
           input_text.label='텍스트를 입력해 주세요'
           page.update()
           return
         
         img = qrcode.make(input_text.value)
         #
         buffer = io.BytesIO()
         img.save(buffer, format='PNG')

         buffer.seek(0)
         
         base64_vreson = base64.b64encode(buffer.read()).decode('utf-8')
         qrcode_image.src_base64 = base64_vreson
         qrcode_image.update()
         
        # 파일로 저장하고 읽기 / 메모리로 저장하기 사용하기
        #  current_dir = os.getcwd() # get dir
        #  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        #  img_path = os.path.join(current_dir, f'qrcode_{timestamp}.jpg')
        #  img.save(img_path)
         
        #  with open(img_path, 'rb') as f:
        #      base64_vreson = base64.b64encode(f.read()).decode('utf-8')
        #      qrcode_image.src_base64 = base64_vreson
        #  qrcode_image.update()
        #  os.remove(img_path)
         
         
     def save_to_file(e):
        current_dir = os.getcwd()
        #save_path = Path.cwd() / (input_text.value + '_qrcode.jpg')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        img_path = os.path.join(current_dir, f'qrcode_{timestamp}.png')
        
        img = qrcode.make(input_text.value)
        img.save(img_path)
        page.snack_bar = ft.SnackBar(ft.Text(f"QR Code saved to {img_path}"), bgcolor=ft.colors.SUCCESS)
        page.snack_bar.open = True
        page.update()
     
     input_text = ft.TextField(label='Enter Text for QRcode', on_submit=create_qr)
     qr_button = ft.IconButton(ft.Icons.ADD, icon_size=40, on_click=create_qr)
     save_button = ft.IconButton(ft.icons.SAVE, icon_size=40, on_click=save_to_file)
     qrcode_image = ft.Image(src='None') # error point, AI don't Know.
     
     
     page.add(
         ft.Column(
         [
         ft.Row([ input_text , qr_button, save_button]),
         qrcode_image
        ], alignment= ft.MainAxisAlignment.CENTER, spacing=20),
    )

ft.app(main)