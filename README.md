# Instagram DM to Discord Webhook Notifier

This project monitors incoming Instagram Direct Messages in real time and forwards new messages to a Discord channel using a webhook.

It supports text messages, photos, voice messages, and Reels (clips).

---

## 🚀 Features

- Real-time Instagram DM monitoring  
- Discord webhook notifications  
- Embedded message previews  
- Photo, voice message, and Reels support  
- Configurable check interval  
- Lightweight and easy to run  

---

## ⚙️ Requirements

- Python 3.9 or newer
- Instagram account
- Discord webhook URL

### Python Dependencies

```bash
pip install instagrapi requests
```

## 🛠️ Configuration

Edit the following variables in the script:
```
IG_USERNAME = 'your_username'
IG_PASSWORD = 'your_password'
DISCORD_WEBHOOK_URL = 'your_discord_webhook'
CHECK_INTERVAL = 40
```

## ▶️ Usage

Run the script with:
```
python main.py
```
Once running, the script will continuously check for new Instagram DMs and send them to your Discord server.

## ⚠️ Disclaimer

This project is for educational purposes only.

Using automation or third-party libraries may violate Instagram’s Terms of Service.
The author is not responsible for any account restrictions or bans.

Use at your own risk.
