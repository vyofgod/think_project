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
- **Çoklu AI Model Desteği ve Yedekleme Stratejisi:** Sistem, yerel bir komut tanınmadığında AI modellerine başvurur. Yanıt almak için sırasıyla Gemini, ChatGPT ve DeepSeek modellerini dener. Bir modelden yanıt alınamazsa otomatik olarak bir sonrakine geçer.

---

## 🛠️ Gereksinimler

- **Python 3.6+**
- **Gemini, ChatGPT, DeepSeek API Anahtarları** (AI modellerini kullanabilmek için gerekli)
- **pip** (Python paket yöneticisi)

---

## 🔧 Başlangıç

### 1. Depoyu Klonlayın

Öncelikle, projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/vyofgod/think_project.git
cd think_project
```

### 2. Bağımlılıkları Yükleyin

Projede kullanılan Python paketlerini yüklemek için:

```bash
pip install -r requirements.txt
```

### 3. API Anahtarlarınızı Ayarlayın

ChatGPT, Gemini ve DeepSeek API'lerini kullanabilmek için geçerli API anahtarlarına ihtiyacınız vardır. Bu anahtarları, projenizin içindeki `think_project/config.py` dosyasında bulunan ilgili alanlara girerek ayarlamanız gerekmektedir.

`think_project/config.py` dosyasını açın ve içerisindeki yer tutucu anahtarları kendi API anahtarlarınızla değiştirin:

```python
# think_project/config.py

# Placeholder for ChatGPT API Key
CHATGPT_API_KEY = 'anahtarınızı_buraya_yapıştırın'

# Placeholder for Gemini API Key
GEMINI_API_KEY = 'anahtarınızı_buraya_yapıştırın'

# Placeholder for DeepSeek API Key
DEEPSEEK_API_KEY = 'anahtarınızı_buraya_yapıştırın'
```

**Önemli Not:** `think_project/config.py` dosyası, güvenlik nedeniyle `.gitignore` dosyasına eklenmiştir. Bu sayede, kişisel API anahtarlarınızın yanlışlıkla Git deposuna gönderilmesi engellenir. Lütfen bu dosyayı kendi ortamınızda düzenleyin ve değişikliklerinizi commit etmeyin.

### 4. Projeyi Çalıştırın

Projeyi başlatmak için aşağıdaki komutu kullanın:

```bash
python think_project/think.py
```
(Not: Eğer `tests` klasörüyle aynı dizindeyseniz (proje ana dizininde) `python -m think_project.think` komutunu kullanmanız daha doğru olabilir.)

### 5. Temel komutlar ve kullanım

- **Uygulama Başlatma:** `firefoxu aç`
  - Açıklama: Firefox tarayıcınız kurulu ise başlatır. (Bu komut, kullandığınız AI modelinin yorumlama yeteneğine göre değişiklik gösterebilir.)
- **Sistem Komutu Çalıştırma:** `komut satırında çalıştır ls -la`
  - Açıklama: Terminalde `ls -la` komutunu çalıştırarak dizin içeriğini listeler. (UYARI: Bu komut, sisteminizde doğrudan bir komut çalıştıracaktır. Güvenli olduğundan emin olmadığınız komutları çalıştırmayın.)
- **Dosya Oluşturma:** `ornek.txt diye dosya oluştur`
  - Açıklama: Geçerli dizinde `ornek.txt` dosyasını oluşturur.
- **Dosya Silme:** `şu dosyayı sil ornek.txt`
  - Açıklama: `ornek.txt` dosyasını siler.

---

### Gelişmiş Kullanım

Think Project, `think_project/think.py` dosyasını düzenleyerek daha fazla komut eklemenize ve özelleştirmenize olanak tanır. Komut eşleştirme mekanizması ve API entegrasyonu sayesinde gelişmiş sistem komutlarını da çalıştırabilirsiniz.

---

### 🤝 Katkı Sağlama

Projeye katkıda bulunmak isterseniz:

1.  **Fork:** Depoyu fork’layın.
2.  **Yeni Bir Branch Oluşturun:** Özellik eklemek veya hata düzeltmesi yapmak için yeni bir branch oluşturun. (`git checkout -b ozellik/yeni-ozellik`)
3.  **Değişikliklerinizi Yapın:** Kod üzerinde gerekli düzenlemeleri yapın.
    *   Komut işleme mantığı (`think_project/think.py` içinde) daha modüler ve bakımı kolay hale getirilmiştir. Lütfen bu yapıya uygun değişiklikler yapmaya özen gösterin.
    *   Projede artık birim testleri (`tests` klasörü altında) bulunmaktadır. Katkıda bulunanların mevcut testlerin geçtiğinden emin olmaları ve yeni özellikler için testler eklemeleri teşvik edilir. Testleri çalıştırmak için proje ana dizinindeyken `python -m unittest discover tests` komutunu kullanabilirsiniz.
4.  **Pull Request Gönderin:** Yaptığınız değişiklikleri proje sahibine göndermek için pull request oluşturun.

---

### 📜 Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır.
