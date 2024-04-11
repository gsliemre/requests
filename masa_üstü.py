import time
import os
from plyer import notification
while True:

    def send_notification(title, message):
        notification.notify(
        title=title,
        message=message,
        app_name="My Notification App",
        timeout=30 # Bildirimin ekranda kalma süresi (saniye cinsinden)
    )

    def main():
     while True:
        try:
            title = input("Bildirim başlığı: ")
            message = input("Bildirim içeriği: ")
            send_notification(title, message)
            print("Bildirim gönderildi!")
            time.sleep(60)  # 1 dakika bekle
        except KeyboardInterrupt:
            print("\nUygulama kapatıldı.")
            break

        if __name__ == "__main__":
            main()
        time.sleep(1*1)