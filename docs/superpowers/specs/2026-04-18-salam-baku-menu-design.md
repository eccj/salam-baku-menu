# Salam Baku Restaurant — Menü Tasarım Spec

**Tarih:** 2026-04-18
**Müşteri:** SALAM BAKU Restaurant (Azerbaycan mutfağı, Kazakistan)
**Yüklenici:** Emre Cetinkaya
**Çıktı:** Basılı PDF menü, 25 sayfa hedefli, pilot 5 sayfa ile başlıyoruz

## 1. Amaç

Salam Baku'nun mevcut yıpranmış, tutarsız tipografili, az fotoğraflı menüsünü **modern, okunaklı, fotoğraf-ağırlıklı, tek tasarım dilinde** bir kitapçık haline getirmek.

**Birincil başarı ölçütü:** Müşteri pilot 5 sayfayı gördüğünde "evet, bu yönde devam edelim" demeli.

## 2. Mevcut Menüden Tespit Edilen Sorunlar

- Kapak ve sayfalar **kırışık, pis, metal halkalarla klasör stili** — yenilenmesi gerekli.
- Sayfa başına genelde **yalnızca 1 küçük fotoğraf**; bazı sayfalarda hiç yok.
- Tipografi: Cyrillic uyumlu zayıf bir serif font, küçük boyut, hiyerarşi zayıf.
- Fotoğraflar dekoratif/diagonal yerleştirilmiş, tutarsız boyutta.
- Fiyat gösterimi tutarsız — bazı satırlarda dikey boşluk kötü.

## 3. Scope (Pilot)

**Pilot 5 sayfa** — müşteri onayından önce:

| # | Sayfa | Kaynak | İçerik |
|---|-------|--------|--------|
| 1 | Kapak | IMG_8278 | Marka, "Меню", minimal süsleme |
| 2 | Салаты с майонезом | IMG_8280 | 9 salata |
| 3 | Первые блюда | IMG_8282 | 12 çorba |
| 4 | Азербайджанская кухня | IMG_8285 | 13 Azerbaycan yemeği |
| 5 | Шашлыки маринованные | IMG_8291 | 13 şiş + 3 alt bölüm (Сет, Рыба, Тандыр) |

**Out of scope (pilot'ta):** Kalan 20 sayfa (Хачапури, Десерты, Хлеб, Соусы, Пицца, Европейская кухня tamamı, Восточная кухня, vb.) — onay sonrası aynı şablon ile üretilecek.

## 4. Tasarım Kararları

### 4.1 Stil: "Bakü Elegance"

Müşteri/kullanıcı seçimi (visual companion A). Şık, klasik, fine-dining havası. Modern Casual/Bistro'dan daha prestijli.

- **Renkler:**
  - `--bg: #faf5ea` (krem arka plan)
  - `--ink: #1a1a1a` (gövde metni)
  - `--wine: #7a2027` (bordo aksan — kategori başlıkları, fiyatlar)
  - `--gold: #b59a4f` (ince süsleme çizgileri, eşkenar dörtgen)
- **Tipografi (Cyrillic-uyumlu):**
  - Display / Başlık: **Playfair Display** (serif, italic/bold/regular)
  - Body: **PT Serif** (okunaklı, klasik Cyrillic)
  - Accent / vurgu / italik: **Cormorant Garamond**
- **Süsleme:** altın eşkenar dörtgen + ince çizgi, minimal

### 4.2 Format

- **Sayfa:** A4 portrait (210 × 297 mm)
- **Cilt:** Kitapçık (telli / iplikli, 4-16 kat — müşteri baskı kararı)
- **Bleeding:** Şimdilik 0 mm (matbaa istenirse eklenecek)

### 4.3 Layout: Kategori sayfası

```
+-------------------------------------------+
|   SALAM BAKU · RESTAURANT (eyebrow)       |
|   КАТЕГОРИЯ (30pt, bordo)                 |
|   Alt başlık italik (serif accent)        |
|   ── ◆ ──  (altın süsleme)                |
|                                           |
|   [item 1]   [item 7]   [foto 1]          |
|   [item 2]   [item 8]                     |
|   [item 3]   [item 9]   [foto 2]          |
|   [item 4]   [item 10]                    |
|   [item 5]   [item 11]                    |
|   [item 6]   [item 12]                    |
|                                           |
|   Обслуживание 10%   · III ·   цены в ₸   |
+-------------------------------------------+
```

- Grid: 2 metin sütunu (1fr 1fr) + 52mm foto rayı
- Items: ad — noktalı çizgi — fiyat + açıklama (italic)
- Footer: hizmet %, sayfa numarası (roman), para birimi notu

### 4.4 Layout: Kapak

Minimal klasik kompozisyon.

- Üstte: alerji bilgilendirme (küçük, dim)
- Merkezde: marka amblem + "SALAM BAKU RESTAURANT" + altın çizgiler + 118pt italik "Меню" + alt başlık
- Altta: "★ · 2026 · ★" + küçük teşekkür satırı

## 5. İçerik ve Dil

- **Dil:** Yalnızca **Rusça** (Kiril). İleride Kazakça/İngilizce eklenmesi mümkün ama pilot'ta değil.
- **Para birimi:** KZT (tenge), `kzt` suffix küçük puntoyla.
- **Fiyat formatı:** binlikler boşlukla ayrılmış (`2 790 kzt`).
- **Açıklamalar:** yalnızca eski menüde olan bilgi; yoksa kısa italik vurgu eklenebilir (örn. "классический цезарь с обжаренной курицей").
- **Alerji notu:** kapakta.

## 6. Fotoğraflar (demo kalite)

**Bilinçli kısıt:** Pilot için yemek fotoğrafları **eski menü sayfalarından kırpıldı**. Çözünürlük düşüktür — baskı için yeterli **değildir**.

Pilot'ta kullanılan 8 fotoğraf:
- salad-caesar, soup-solyanka, soup-ramen, az-khashlama, az-piti, shashlik-mix, shashlik-fish, cover-logo-bg

**Karar gerektiren:** Son baskı için fotoğraflar yeniden mi çekilecek, yoksa stock mu kullanılacak? Müşterinin pilot'u onaylamasından sonra konuşulacak.

## 7. Teknik Yaklaşım

- **Kaynak:** Tek HTML dosyası (`src/index.html`) + tek CSS dosyası (`src/styles.css`)
- **İçerik verisi:** `content/pilot.json` (şu an HTML'e inline gömülü; 25 sayfaya çıkarken generator script yazılabilir)
- **Baskı:** `@page A4 portrait; margin: 0` + `.page { width: 210mm; height: 297mm }`
- **Fontlar:** Google Fonts CDN (Playfair Display + PT Serif + Cormorant Garamond, cyrillic subset)
- **PDF render:** Headless Chrome (`render.sh` script'i)

```bash
./render.sh  # → output/pilot.pdf
```

## 8. Scope-Out (şimdi yapılmayacak)

- Kazakça/İngilizce çeviri
- Fiyatların herhangi bir sistemle senkronizasyonu
- Online/QR menü
- Profesyonel yemek fotoğrafçılığı
- Matbaa bleed/trim ayarları
- Kalan 20 sayfa (pilot onayı sonrası)
- Restoran logosunun profesyonel vektör versiyonu (şimdi placeholder SVG kullanıldı)

## 9. Riskler

| Risk | Sınıf | Azaltma |
|------|-------|---------|
| Müşteri stili beğenmez | Yüksek | Pilot ile %100 ön-validasyon |
| Fotoğraflar baskı kalitesi yetersiz | Yüksek | Müşteriyle açık iletişim; yeni çekim/stock planı |
| Uzun Cyrillic yemek adları dar sütuna sığmaz | Orta | `min-width: 0` + wrap + 2 satır kabul |
| Sayfa 5 (şişler) içerik yoğun | Orta | Subsection font'ları küçültüldü, 3 alt-bölüm tek sayfada |

## 10. Kabul Kriterleri

Pilot PDF şu koşulları sağlar:
- [x] 5 sayfa, her biri A4
- [x] Cyrillic karakterler düzgün render
- [x] Her kategori sayfasında ≥ 1 fotoğraf (3 sayfada 2 foto)
- [x] Tek tasarım dili — kapak ve iç sayfalar birlikte aitlik hissi veriyor
- [x] Fiyatlar, kategoriler, ürün adları eski menüyle eşleşiyor
- [x] Renkler, tipografi, süslemeler tutarlı

## 11. Onaydan Sonra Yapılacaklar

1. Müşteri pilot.pdf'i inceler
2. Gereken yön/stil değişiklikleri uygulanır
3. Kalan 20 sayfanın OCR içeriği çıkarılır (`content/all.json`)
4. Şablonla tüm sayfalar üretilir
5. Kapak arka yüz + içindekiler sayfası eklenir
6. Matbaa versiyonu için bleed/trim ayarlanır
7. Fotoğraf çekimi/stock kararı uygulanır
