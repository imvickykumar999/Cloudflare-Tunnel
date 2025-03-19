# `Cloudflare Tunnel`

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver 8080
cloudflared tunnel run termux-tunnel
```
