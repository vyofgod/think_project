# Think Project

**Think Project**, bilgisayarınızı sadece bir yapay zeka aracılığıyla kullanmanıza olanak tanıyan, terminal tabanlı bir projedir. Bu proje, yapay zeka komutları ile sistem komutlarını çalıştırmayı, uygulamaları başlatmayı ve dosya işlemleri gerçekleştirmeyi sağlar.

---

## 🚀 Proje Amacı

Bilgisayarınızı geleneksel yollarla kullanmak yerine, bir yapay zeka aracılığıyla yönetmek istiyoruz. Proje, düşük donanımlı cihazlarda bile verimli çalışacak şekilde optimize edilmiştir. Mevcut AI ajanlarının yüksek kaynak tüketimine karşı, Think Project daha hafif ve verimli bir çözüm sunar.

---

## ⚡️ Özellikler

- **AI Tabanlı Sistem Yönetimi:** Yapay zeka ile bilgisayarınızda işlem yapma.
- **Terminal Tabanlı Kullanım:** Komutlarınızı terminal üzerinden çalıştırma.
- **Düşük Kaynak Kullanımı:** Minimal donanım gereksinimleri.
- **Dosya Yönetimi:** Dosya açma, oluşturma, silme, taşıma, kopyalama, ad değiştirme ve içeriği gösterme.

---

## 🛠️ Gereksinimler

- **Python 3.6+**
- **Gemini, ChatGPT, DeepSeek API** (AI modellerini kullanabilmek için gerekli)
- **pip** (Python paket yöneticisi)

---

## 🔧 Başlangıç

### 1. Depoyu Klonlayın

Öncelikle, projeyi bilgisayarınıza klonlayın:

git clone https://github.com/vyofgod/think_project.git
cd think_project

### 2. Bağımlılıkları Yükleyin

Projede kullanılan Python paketlerini yüklemek için:

pip install -r requirements.txt

### 3. API Anahtarınızı Ayarlayın

ChatGPT, Gemini ve DeepSeek API'lerini kullanabilmek için geçerli bir API anahtarına ihtiyacınız var. API anahtarlarınızı ilgili platformlardan alarak, bu anahtarları config.py dosyasına ekleyin.

ChatGPT API anahtarı
CHATGPT_API_KEY = 'anahtarınızı_buraya_yapıştırın'

Gemini API anahtarı
GEMINI_API_KEY = 'anahtarınızı_buraya_yapıştırın'

DeepSeek API anahtarı
DEEPSEEK_API_KEY = 'anahtarınızı_buraya_yapıştırın'

### 4. Projeyi Çalıştırın

Projeyi başlatmak için aşağıdaki komutu kullanın:

python think.py

### 5. Temel komutlar ve kullanım

Uygulama Başlatma: firefoxu aç (şu an en sağlıklı çalışan komut bu, yanıtlar apiden şekillendiği için örnek olsun diye bu komutu verdim bağlayacağınız yapay zekaya.)
Açıklama: Firefox tarayıcınız kurulu ise başlatır.

Sistem Komutu Çalıştırma: çalıştır 'ls -la'
Açıklama: Terminalde ls -la komutunu çalıştırarak dizin içeriğini listeler.

Dosya Oluşturma: ornek.txt diye dosya oluştur.
Açıklama: Geçerli dizinde ornek.txt dosyasını oluşturur.

Dosya Silme: şu dosyayı sil ornek.txt
Açıklama: ornek.txt dosyasını siler.

---

### Gelişmiş Kullanım;
Think Project, think.py dosyasını düzenleyerek daha fazla komut eklemenize ve özelleştirmenize olanak tanır. Komut eşleştirme mekanizması ve API entegrasyonu sayesinde gelişmiş sistem komutlarını da çalıştırabilirsiniz.

---


### 🤝 Katkı Sağlama
Projeye katkıda bulunmak isterseniz:

Fork: Depoyu fork’layın.
Yeni Bir Branch Oluşturun: Özellik eklemek veya hata düzeltmesi yapmak için yeni bir branch oluşturun.
Pull Request Gönderin: Yaptığınız değişiklikleri proje sahibine göndermek için pull request oluşturun.


### 📜 Lisans
Bu proje, MIT Lisansı altında lisanslanmıştır.
