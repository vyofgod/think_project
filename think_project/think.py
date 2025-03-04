import requests
import subprocess
import os
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

def send_to_gemini(command):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAq_t6KpyXpb5INbLtrJvNQCWcpAo00FQU"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{"parts": [{"text": command}]}]
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['candidates'][0]['content']['parts'][0]['text']
    else:
        print("API Hatası:", response.status_code)
        print(response.text)
        return "API çağrısı başarısız oldu."

def run_system_command(command):
    cmd = command.lower()
    try:
        if "firefox" in cmd and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["firefox"])
            print("Tamamdır, Firefox'u açıyorum.")
        elif ("chrome" in cmd or "google chrome" in cmd) and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["google-chrome"])
            print("Tamamdır, Google Chrome'u açıyorum.")
        elif "gimp" in cmd and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["gimp"])
            print("Tamamdır, GIMP'i açıyorum.")
        elif "libreoffice" in cmd and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["libreoffice"])
            print("Tamamdır, LibreOffice'i açıyorum.")
        elif "gedit" in cmd and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["gedit"])
            print("Tamamdır, Gedit'i açıyorum.")
        elif ("vscode" in cmd or "visual studio code" in cmd) and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["code"])
            print("Tamamdır, Visual Studio Code'u açıyorum.")
        elif "nautilus" in cmd and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["nautilus"])
            print("Tamamdır, Nautilus'u açıyorum.")
        elif "spotify" in cmd and ("aç" in cmd or "başlat" in cmd):
            subprocess.Popen(["spotify"])
            print("Tamamdır, Spotify'ı açıyorum.")

        elif "dosya" in cmd:
            if "aç" in cmd:
                parts = command.split("aç", 1)
                if len(parts) > 1:
                    filename = parts[1].strip()
                    if os.path.exists(filename):
                        subprocess.Popen(["xdg-open", filename])
                        print(f"{filename} dosyasını açıyorum.")
                    else:
                        print(f"{filename} dosyası bulunamadı.")
                else:
                    print("Dosya adı belirtilmedi.")
            elif "oluştur" in cmd or "yarat" in cmd:
                if "oluştur" in cmd:
                    parts = command.split("oluştur", 1)
                else:
                    parts = command.split("yarat", 1)
                if len(parts) > 1:
                    filename = parts[1].strip()
                    with open(filename, "w") as file:
                        file.write("")
                    print(f"{filename} dosyasını oluşturuyorum.")
                else:
                    print("Dosya adı belirtilmedi.")
            elif "sil" in cmd:
                parts = command.split("sil", 1)
                if len(parts) > 1:
                    filename = parts[1].strip()
                    if os.path.exists(filename):
                        os.remove(filename)
                        print(f"{filename} dosyası silindi.")
                    else:
                        print(f"{filename} dosyası bulunamadı.")
                else:
                    print("Dosya adı belirtilmedi.")
            elif "taşı" in cmd:
                parts = command.split()
                try:
                    idx = parts.index("taşı")
                    filename = parts[idx + 1]
                    target = parts[idx + 2]
                    subprocess.run(["mv", filename, target])
                    print(f"{filename} dosyasını {target} klasörüne taşıdım.")
                except Exception as e:
                    print(f"Dosya taşıma hatası: {e}")
            elif "kopyala" in cmd:
                parts = command.split()
                try:
                    idx = parts.index("kopyala")
                    filename = parts[idx + 1]
                    target = parts[idx + 2]
                    subprocess.run(["cp", filename, target])
                    print(f"{filename} dosyasını {target} klasörüne kopyaladım.")
                except Exception as e:
                    print(f"Dosya kopyalama hatası: {e}")
            elif "ad değiştir" in cmd:
                parts = command.split()
                try:
                    idx = parts.index("değiştir")
                    old_name = parts[idx + 1]
                    new_name = parts[idx + 2]
                    os.rename(old_name, new_name)
                    print(f"{old_name} dosyasının adını {new_name} olarak değiştirdim.")
                except Exception as e:
                    print(f"Dosya ad değişikliği hatası: {e}")
            elif "içeriği göster" in cmd:
                parts = command.split("içeriği göster", 1)
                if len(parts) > 1:
                    filename = parts[1].strip()
                    if os.path.exists(filename):
                        with open(filename, "r") as file:
                            content = file.read()
                        print(content)
                    else:
                        print(f"{filename} dosyası bulunamadı.")
                else:
                    print("Dosya adı belirtilmedi.")
        
        elif "sistem durumu" in cmd:
            print("Sistem durumu bilgileri:")
            print(subprocess.getoutput("top -n 1"))
        
        elif "komut satırında çalıştır" in cmd:
            parts = command.split("çalıştır", 1)
            if len(parts) > 1:
                sys_command = parts[1].strip()
                output = subprocess.getoutput(sys_command)
                print(output)
            else:
                print("Çalıştırılacak komut belirtilmedi.")
        

        elif "sistemi yeniden başlat" in cmd:
            subprocess.run(["reboot"])
        elif "sistemi kapat" in cmd:
            subprocess.run(["shutdown", "now"])
        
        elif "çalışan uygulamaları göster" in cmd:
            print(subprocess.getoutput("ps aux"))
        
        elif "uygulama kapat" in cmd or "uygulama öldür" in cmd:
            parts = command.split()
            try:
                if "kapat" in parts:
                    idx = parts.index("kapat")
                else:
                    idx = parts.index("öldür")
                app_name = parts[idx + 1]
                subprocess.run(["pkill", app_name])
                print(f"{app_name} uygulamasını kapatıyorum.")
            except Exception as e:
                print(f"Uygulama kapatma hatası: {e}")
        
        elif "neler yapabiliyorsun?" in cmd:
            print("Benim yapabileceğim işlemler şunlardır:")
            print("- Uygulama başlatma: Firefox, Chrome, GIMP, LibreOffice, VSCode, Nautilus, Spotify vb.")
            print("- Dosya yönetimi: Dosya açma, oluşturma, silme, taşıma, kopyalama, ad değiştirme, içeriği gösterme.")
            print("- Sistem bilgisi alma: CPU, RAM, disk, ağ durumu vb.")
            print("- Yazılım yükleme, kaldırma ve güncelleme (sistem komutları ile).")
            print("- Ağ ve internet işlemleri: Ping atma, IP sorgulama vb.")
            print("- Terminal komutlarını çalıştırma, sistemi yeniden başlatma veya kapatma vb.")
        
        else:
            print("Bilmiyorum, başka bir şey deneyebilirsiniz.")
    except Exception as e:
        print(f"Komut çalıştırılamadı: {e}")

def process_command_wrapper(command):
    triggers = [
        "aç", "başlat", "oluştur", "yarat", "dosya", "sil", "taşı", "kopyala", "değiştir",
        "içeriği göster", "sistem durumu", "komut satırında çalıştır", "sistemi yeniden başlat",
        "sistemi kapat", "çalışan uygulamaları göster", "uygulama kapat", "uygulama öldür", "neler yapabiliyorsun?"
    ]
    if any(trigger in command.lower() for trigger in triggers):
        run_system_command(command)
    else:
        result = send_to_gemini(command)
        print(result)

style = Style.from_dict({
    "": "#ffffff",
    "prompt": "#00ff00 bold",
})

def main():
    print("╭── Think Terminal ───╮")
    print("│ ✻ Welcome to Think! │")
    print("╰─────────────────────╯")
    
    while True:
        user_input = prompt("❯ ", style=style)
        if user_input.lower() == "exit":
            print("Çıkılıyor...")
            break
        process_command_wrapper(user_input)

if __name__ == "__main__":
    main()
