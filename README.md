># `Cloudflare Tunnel`
>
>![WhatsApp Image 2025-03-19 at 10 36 39_dc4c8ea3](https://github.com/user-attachments/assets/5e4f1683-6673-42fd-a01d-5a7e41cd22ec)

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

pkg update && pkg upgrade
pkg install libjpeg-turbo libpng zlib
pip install Pillow

python manage.py runserver 8080
cloudflared tunnel run termux-tunnel
```
