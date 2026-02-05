import time
import requests
from instagrapi import Client

# --- SETTINGS ---
IG_USERNAME = 'your_username'
IG_PASSWORD = 'your_password'
DISCORD_WEBHOOK_URL = 'your_discord_webhook'
CHECK_INTERVAL = 40  # delay in seconds

cl = Client()

try:
    print("Logging into Instagram...")
    cl.login(IG_USERNAME, IG_PASSWORD)
    my_user_id = cl.user_id
    print(f"Login successful! Your user ID: {my_user_id}")
except Exception as e:
    print(f"Login failed: {e}")
    exit()

def send_to_discord(user, message_content, media_url=None):
    clean_media_url = str(media_url) if media_url else None
    
    embed = {
        "title": "📸 New Instagram Message!",
        "description": f"**Sender:** {user}\n**Message:** {message_content}",
        "color": 15418782
    }
    
    if clean_media_url:
        embed["image"] = {"url": clean_media_url}

    data = {
        "content": "@everyone",
        "embeds": [embed],
        "allowed_mentions": {"parse": ["everyone"]}
    }
    
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Successfully sent to Discord.")
    else:
        print(f"Discord error: {response.status_code} - {response.text}")

last_checked_msg_id = None
print("Listening for new messages...")

while True:
    try:
        threads = cl.direct_threads(1)
        if threads:
            last_thread = threads[0]
            last_message = last_thread.messages[0]

            if last_checked_msg_id is None:
                last_checked_msg_id = last_message.id
                print("System is ready.")

            if last_message.id != last_checked_msg_id:
                if str(last_message.user_id) != str(my_user_id):
                    username = last_thread.users[0].username if last_thread.users else "Unknown"
                    
                    text = last_message.text or ""
                    media_url = None

                    if last_message.item_type == 'media':
                        media_url = str(last_message.media.thumbnail_url)
                        text += "\n*(Photo sent)*"
                    elif last_message.item_type == 'voice_media':
                        media_url = str(last_message.voice_media.media.audio_src)
                        text += f"\n🎤 **Voice Message:** {media_url}"
                    elif last_message.item_type == 'clip':
                        media_url = str(last_message.clip.thumbnail_url)
                        text += f"\n🎬 **Reels Video:** {str(last_message.clip.video_url)}"

                    print(f"NEW MESSAGE: {username} -> {text}")
                    send_to_discord(username, text, media_url)
                
                last_checked_msg_id = last_message.id
        
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(10)
    
    time.sleep(CHECK_INTERVAL)
