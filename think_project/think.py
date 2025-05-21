import requests
import subprocess
import os
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from think_project.config import CHATGPT_API_KEY, GEMINI_API_KEY, DEEPSEEK_API_KEY

def send_to_chatgpt(command):
    url = f"https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHATGPT_API_KEY}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": command}],
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        print("API Hatası:", response.status_code)
        print(response.text)
        return "API çağrısı başarısız oldu."

def send_to_gemini(command):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
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

def send_to_deepseek(command):
    url = f"https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": command}],
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        print("API Hatası:", response.status_code)
        print(response.text)
        return "API çağrısı başarısız oldu."

# --- Helper function for launching applications ---
def _launch_application(cmd, app_name, command_aliases, process_name):
    if any(alias in cmd for alias in command_aliases) and \
       ("aç" in cmd or "başlat" in cmd):
        try:
            subprocess.Popen([process_name])
            print(f"Tamamdır, {app_name}'i açıyorum.")
            return True
        except Exception as e:
            print(f"{app_name} başlatılırken hata oluştu: {e}")
            return True # Command was handled, even if it failed
    return False

# --- Helper functions for file operations ---
def _handle_file_open(command):
    parts = command.split("aç", 1)
    if len(parts) > 1:
        filename = parts[1].strip()
        if os.path.exists(filename):
            try:
                subprocess.Popen(["xdg-open", filename])
                print(f"{filename} dosyasını açıyorum.")
            except Exception as e:
                print(f"Dosya açılırken hata: {e}")
        else:
            print(f"{filename} dosyası bulunamadı.")
    else:
        print("Dosya adı belirtilmedi.")

def _handle_file_create(command):
    if "oluştur" in command:
        parts = command.split("oluştur", 1)
    elif "yarat" in command:
        parts = command.split("yarat", 1)
    else:
        print("Dosya adı belirtilmedi.") # Should not happen if called correctly
        return

    if len(parts) > 1:
        filename = parts[1].strip()
        try:
            with open(filename, "w") as file:
                file.write("")
            print(f"{filename} dosyasını oluşturuyorum.")
        except Exception as e:
            print(f"Dosya oluşturulurken hata: {e}")
    else:
        print("Dosya adı belirtilmedi.")

def _handle_file_delete(command):
    parts = command.split("sil", 1)
    if len(parts) > 1:
        filename = parts[1].strip()
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"{filename} dosyası silindi.")
            except Exception as e:
                print(f"Dosya silinirken hata: {e}")
        else:
            print(f"{filename} dosyası bulunamadı.")
    else:
        print("Dosya adı belirtilmedi.")

def _handle_file_move(command):
    parts = command.split()
    try:
        idx = parts.index("taşı")
        if len(parts) > idx + 2:
            filename = parts[idx + 1]
            target = parts[idx + 2]
            subprocess.run(["mv", filename, target])
            print(f"{filename} dosyasını {target} klasörüne taşıdım.")
        else:
            print("Taşıma için dosya adı veya hedef belirtilmedi.")
    except ValueError:
        print("Taşıma komutu hatalı.") # "taşı" keyword not found
    except Exception as e:
        print(f"Dosya taşıma hatası: {e}")

def _handle_file_copy(command):
    parts = command.split()
    try:
        idx = parts.index("kopyala")
        if len(parts) > idx + 2:
            filename = parts[idx + 1]
            target = parts[idx + 2]
            subprocess.run(["cp", filename, target])
            print(f"{filename} dosyasını {target} klasörüne kopyaladım.")
        else:
            print("Kopyalama için dosya adı veya hedef belirtilmedi.")
    except ValueError:
        print("Kopyalama komutu hatalı.")
    except Exception as e:
        print(f"Dosya kopyalama hatası: {e}")

def _handle_file_rename(command):
    parts = command.split()
    try:
        # Try to find "ad değiştir" phrase for more robust parsing
        cmd_lower_parts = [p.lower() for p in parts]
        phrase_idx = -1
        
        # Search for "ad değiştir"
        for i in range(len(cmd_lower_parts) - 1):
            if cmd_lower_parts[i] == "ad" and cmd_lower_parts[i+1] == "değiştir":
                # Check if there are enough parts after "ad değiştir" for old and new names
                if len(parts) > i + 3: # parts[i] is "ad", parts[i+1] is "değiştir"
                    phrase_idx = i
                    old_name = parts[i+2]
                    new_name = parts[i+3]
                    os.rename(old_name, new_name)
                    print(f"{old_name} dosyasının adını {new_name} olarak değiştirdim.")
                    return
                else:
                    print("Ad değiştirme komutu için eski ve yeni adlar eksik.")
                    return
        
        # Fallback for "ESKI_AD adını YENI_AD olarak değiştir"
        if "adını" in cmd_lower_parts and "olarak" in cmd_lower_parts and "değiştir" in cmd_lower_parts:
            try:
                idx_adini = cmd_lower_parts.index("adını")
                idx_olarak = cmd_lower_parts.index("olarak")
                # Basic check: old_name is before "adını", new_name is before "olarak"
                if idx_adini > 0 and idx_olarak > idx_adini + 1 :
                    old_name = parts[idx_adini -1]
                    new_name = parts[idx_olarak -1] # Word before "olarak"
                    os.rename(old_name, new_name)
                    print(f"{old_name} dosyasının adını {new_name} olarak değiştirdim.")
                    return
                else:
                    print("Ad değiştirme komutu ('adını ... olarak değiştir') anlaşılamadı.")
                    return
            except (ValueError, IndexError):
                print("Ad değiştirme komutu ('adını ... olarak değiştir') ayrıştırılamadı.")
                return
        
        # If specific phrases aren't found, use original simpler logic (less robust)
        # This part might be removed if the above are considered sufficient
        if 'değiştir' in cmd_lower_parts:
            idx = cmd_lower_parts.index("değiştir")
            # This assumes "değiştir old new" which is not very robust
            if len(parts) > idx + 2:
                old_name = parts[idx + 1] 
                new_name = parts[idx + 2]
                os.rename(old_name, new_name)
                print(f"{old_name} dosyasının adını {new_name} olarak değiştirdim.")
                return
            else:
                print("Ad değiştirme için eski veya yeni ad belirtilmedi (genel).")
                return
        
        print("Ad değiştirme komutu anlaşılamadı.")

    except FileNotFoundError:
        print(f"Dosya bulunamadı: {old_name}")
    except Exception as e:
        print(f"Dosya ad değişikliği hatası: {e}")


def _handle_file_show_content(command):
    parts = command.split("içeriği göster", 1)
    if len(parts) > 1:
        filename = parts[1].strip()
        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    content = file.read()
                print(content)
            except Exception as e:
                print(f"Dosya içeriği okunurken hata: {e}")
        else:
            print(f"{filename} dosyası bulunamadı.")
    else:
        print("Dosya adı belirtilmedi.")

# --- Refactored run_system_command ---
def run_system_command(command):
    cmd = command.lower()
    
    applications = [
        ("Firefox", ["firefox"], "firefox"),
        ("Google Chrome", ["chrome", "google chrome"], "google-chrome"),
        ("GIMP", ["gimp"], "gimp"),
        ("LibreOffice", ["libreoffice"], "libreoffice"),
        ("Gedit", ["gedit"], "gedit"),
        ("Visual Studio Code", ["vscode", "visual studio code"], "code"),
        ("Nautilus", ["nautilus"], "nautilus"),
        ("Spotify", ["spotify"], "spotify"),
    ]

    try:
        # 1. Application Launching Logic
        for app_name, aliases, process_name in applications:
            if _launch_application(cmd, app_name, aliases, process_name):
                return

        # 2. File Operations Logic
        # Check for keywords that indicate a file operation.
        file_op_keywords = ["dosya", "içeriği göster"] # "içeriği göster" can be standalone
        if any(kw in cmd for kw in file_op_keywords):
            if "aç" in cmd and ("dosya" in cmd or "dosyasını aç" in cmd): # "dosya aç" or "X dosyasını aç"
                _handle_file_open(command) # Pass original command for parsing
            elif ("oluştur" in cmd or "yarat" in cmd) and "dosya" in cmd:
                _handle_file_create(command)
            elif "sil" in cmd and "dosya" in cmd:
                _handle_file_delete(command)
            elif "taşı" in cmd and "dosya" in cmd: 
                _handle_file_move(command)
            elif "kopyala" in cmd and "dosya" in cmd:
                _handle_file_copy(command)
            elif "ad değiştir" in cmd: # "dosya ad değiştir" or "X adını Y olarak değiştir"
                 _handle_file_rename(command)
            elif "içeriği göster" in cmd: 
                _handle_file_show_content(command)
            # If "dosya" was in cmd, but none of the above matched, we might want a fallback.
            # However, the original code didn't have a generic "unknown file operation" message.
            # So, if it's not one of these, it will fall through to other system commands or "Bilmiyorum".
            return # File operations handled or attempted

        # 3. Other System Commands
        elif "sistem durumu" in cmd:
            print("Sistem durumu bilgileri:")
            print(subprocess.getoutput("top -n 1"))
        elif "komut satırında çalıştır" in cmd:
            parts = command.split("çalıştır", 1) # Assumes "komut satırında çalıştır XYZ"
            if len(parts) > 1:
                sys_command = parts[1].strip()
                if sys_command: # Ensure it's not empty
                    print("UYARI: Bu komut, sisteminizde doğrudan bir komut çalıştıracaktır. Güvenli olduğundan emin olmadığınız komutları çalıştırmayın.")
                    output = subprocess.getoutput(sys_command)
                    print(output)
                else:
                    print("Çalıştırılacak komut belirtilmedi.")
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
                action_word = ""
                if "kapat" in parts:
                    action_word = "kapat"
                elif "öldür" in parts:
                    action_word = "öldür"
                
                if action_word:
                    idx = parts.index(action_word)
                    if len(parts) > idx + 1:
                        app_name_to_kill = parts[idx + 1]
                        subprocess.run(["pkill", app_name_to_kill])
                        print(f"{app_name_to_kill} uygulamasını kapatıyorum.")
                    else:
                        print("Kapatılacak uygulama adı belirtilmedi.")
                else:
                    # This case should ideally not be reached if "uygulama kapat/öldür" is in cmd
                    print("Uygulama kapatma komutu anlaşılamadı.")
            except ValueError: # If .index fails
                 print("Uygulama kapatma komutu hatalı.")
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
            # Fallback if no other specific command is recognized by run_system_command
            # This is where it ends up if a command like "dosya xyz" (unknown file op) is given
            # and not handled by any of the file helper calls.
            # The original code would also print "Bilmiyorum..." for such cases.
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
        # Sequential fallback for AI models
        error_message = "API çağrısı başarısız oldu."
        result = send_to_gemini(command)

        if result == error_message:
            print("Gemini API başarısız oldu, ChatGPT deneniyor...")
            result = send_to_chatgpt(command)
        
        if result == error_message:
            print("ChatGPT API başarısız oldu, DeepSeek deneniyor...")
            result = send_to_deepseek(command)
            
        if result == error_message:
            print("Tüm AI modelleriyle iletişim kurulamadı.")
        else:
            # Only print the result if it's not the generic error message from the last attempt
            # or if it's a successful response from one of the models.
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
