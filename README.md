# spurious-correlations-colormnist-waterbirds
# Spurious Correlations in Colored MNIST and Waterbirds

**Author:** Kosar Zarean

**Paper:** [تشخیص و کاهش همبستگی‌های کاذب در طبقه‌بندی تصاویر: یک مطالعه تجربی جامع روی Colored MNIST و Waterbirds]

---

## 📌 خلاصه

این مخزن شامل کد، داده خام، و اسکریپت‌های بازتولید مقاله است. همه اعداد، جدول‌ها و شکل‌های مقاله از فایل‌های `results/*/results.json` (یا معادل آن‌ها) بازتولید می‌شوند.

**⚠️ توجه مهم:** این مقاله یک **مطالعه تجربی** است، نه معرفی روش جدید. سهم آن مقایسه نظام‌مند پنج روش کاهش سوگیری در طیف کامل ρ و دو طراحی Colored MNIST است.

---

## 📓 نگاشت نوت‌بوک‌ها به جدول‌های مقاله

هر جدول/شکل مقاله از یک نوت‌بوک مشخص (و خروجی JSON آن) بازتولید می‌شود. جدول زیر این نگاشت را نشان می‌دهد:

| # | نوت‌بوک | معماری / نسخه | خروجی JSON | جدول‌های مقاله | شکل‌های مقاله |
|---|---|---|---|---|---|
| ۱ | `پروژه_رنگی_mnist.ipynb` | **CNN3** (مقاله اصلی) | `results/raw_results_5seed.json` | **۲، ۳، ۴، ۵، ۶، ۷، ۸، ۱۱، ۱۴** | **۲، ۳، ۴، ۵، ۶، ۷، ۸، ۹، ۱۰، ۱۱، ۱۲، ۱۳** |
| ۲ | `coloured_mnist_rho099 (1).ipynb` | **CNN3، ρ=0.99** | `results_rho099/results.json` | ۵ (ستون ρ=0.99) | — |
| ۳ | `color_mnist_light.ipynb` | **CNN2** | `results_light/results.json` | ۵ (ستون CNN2) | — |
| ۴ | `colorful_mnist_minimal.ipynb` | نسخه حداقلی | `results_minimal/results.json` | (مطالعه تکمیلی) | — |
| ۵ | `coloured_mnist_mlp_rho09.ipynb` | **MLP، ρ=0.9** | `results_mlp_rho09/results.json` | ۵ (ستون MLP ρ=0.9) | — |
| ۶ | `coloured_mnist_mlp_rho99.ipynb` | **MLP، ρ=0.99** | `results_mlp_rho99/results.json` | ۵ (ستون MLP ρ=0.99) | — |
| ۷ | `colorful_mnist_10colors.ipynb` | **۱۰ رنگ** | `results_10color/results.json` | **۹، ۱۰، ۱۱** (نسخه ۱۰ رنگ) | — |
| ۸ | `آزمایش‌های کاغذی.ipynb` | آزمایش‌های تکمیلی | `results_paper/results.json` | (مطالعه تکمیلی) | — |
| ۹ | `پرندگان آبزی_آزمایش.ipynb` | **Waterbirds** | `results_waterbirds/waterbirds.json` | **۱۲** | — |

### توضیح جدول‌ها

| جدول | محتوا | نوت‌بوک منبع | اسکریپت بازتولید |
|---|---|---|---|
| جدول ۱-ب | توزیع رنگ/برچسب | `projeh_rangi_mnist.ipynb` | `src/reproduce_table1b.py` |
| جدول ۲ | ارزیابی مدل پایه | `projeh_rangi_mnist.ipynb` | `src/reproduce_table5.py` (بخش Baseline) |
| جدول ۳ | Counterfactual | `projeh_rangi_mnist.ipynb` | `src/reproduce_table6.py` |
| جدول ۴ | Misspecification | `projeh_rangi_mnist.ipynb` | `src/reproduce_table6.py` |
| جدول ۵ | دقت ID/OOD/شکاف | `projeh_rangi_mnist.ipynb` (CNN3) + `results_*` | `src/reproduce_table5.py` |
| جدول ۶ | اثر Dropout | `projeh_rangi_mnist.ipynb` | `src/reproduce_table9.py` |
| جدول ۷ | اتحاد و MAE | `projeh_rangi_mnist.ipynb` | `src/reproduce_table7.py` |
| جدول ۸ | خطای هر رقم | `projeh_rangi_mnist.ipynb` | `src/reproduce_table5.py` (بخش conf) |
| جدول ۹ | روش‌ها (۱۰ رنگ) | `colorful_mnist_10colors.ipynb` | `src/reproduce_table10_10color.py` |
| جدول ۱۰ | پروفایل تکیه بر رنگ (دورنگ) | `projeh_rangi_mnist.ipynb` | `src/reproduce_table10.py` |
| جدول ۱۱ | مقایسه روش‌ها | `projeh_rangi_mnist.ipynb` | `src/reproduce_table11.py` |
| جدول ۱۲ | Waterbirds | `parandegan_abi.ipynb` | `src/reproduce_table12.py` |
| جدول ۱۳ | مقایسه دو طراحی | (تلفیق ۹ و ۱۱) | `src/reproduce_table11.py` |
| جدول ۱۴ | مقایسه با کارهای پیشین | (دستی) | (در مقاله ثابت) |

---

## 🚀 نصب و اجرا

### پیش‌نیازها

- Python 3.10+
- pip

### نصب

```bash
git clone https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds.git
cd spurious-correlations-colormnist-waterbirds
pip install -r requirements.txt
```

### بازتولید همه جدول‌ها و شکل‌ها

```bash
python src/reproduce_all_tables.py
```

خروجی‌ها در `results/` ذخیره می‌شوند:
- `results/table*.csv` — جدول‌ها
- `results/figures/*.png` — شکل‌ها

### بازتولید یک جدول خاص

```bash
# جدول ۵ (مدل پایه)
python src/reproduce_table5.py

# جدول ۷ (اتحاد و MAE)
python src/reproduce_table7.py

# جدول ۱۱ (مقایسه روش‌ها)
python src/reproduce_table11.py

# جدول ۱۲ (Waterbirds)
python src/reproduce_table12.py --results results_waterbirds/waterbirds.json

# شکل‌ها
python src/reproduce_figures.py
```

### بازتولید از نوت‌بوک

اگر می‌خواهی از صفر بازتولید کنی:

1. هر نوت‌بوک را در Colab باز کن (Runtime → GPU)
2. همه سلول‌ها را اجرا کن (Run all)
3. فایل `results.json` (یا معادل آن) را در پوشه مربوطه ذخیره کن
4. اسکریپت بازتولید را اجرا کن

**زمان تقریبی اجرای کامل روی T4 GPU:** ۴۰–۶۰ دقیقه برای هر نوت‌بوک.

---

## 📊 داده خام

همه فایل‌های JSON خام در پوشه‌های `results*/` قرار دارند:

| فایل | توضیح | تعداد seed |
|---|---|---|
| `results/raw_results_5seed.json` | نتایج CNN3 (مقاله اصلی) | ۵ |
| `results/raw_results_3seed.json` | نتایج CNN3 (۳ seed) | ۳ |
| `results_rho099/results.json` | CNN3 با ρ=0.99 | ۵ |
| `results_light/results.json` | CNN2 | ۵ |
| `results_mlp_rho09/results.json` | MLP با ρ=0.9 | ۵ |
| `results_mlp_rho99/results.json` | MLP با ρ=0.99 | ۵ |
| `results_10color/results.json` | نسخه ۱۰ رنگ | ۳ |
| `results_waterbirds/waterbirds.json` | Waterbirds | ۳ |
| `results_minimal/results.json` | نسخه حداقلی | ۳ |
| `results_paper/results.json` | آزمایش‌های تکمیلی | متغیر |

### ساختار JSON

کلیدها به شکل `"{arch}|{rho}|{dropout}|{seed}"` هستند:

```json
{
  "MLP|0.5|0.5|0": {
    "train": 0.9969,
    "val": 0.9701,
    "id": 0.9731,
    "ood1": 0.9733,
    "ood2": 0.9745,
    "id_aligned": 0.9706,
    "id_conflict": 0.9756,
    "swap_acc": 0.9746,
    "color_effect": 0.0139,
    "conf_ood2": [[968, 0, 1, ...], ...]
  },
  ...
}
```

مقادیر دقت در بازه ۰–۱ هستند (ضرب در ۱۰۰ برای درصد).

---

## 📁 ساختار پروژه

```
spurious-correlations-colormnist-waterbirds/
├── README.md                    # این فایل
├── requirements.txt             # وابستگی‌ها
├── REPRODUCIBILITY_REPORT.md    # گزارش بازتولید
├── LICENSE                      # مجوز MIT
│
├── *.ipynb                      # نوت‌بوک‌های Colab
│
├── src/                         # کد بازتولید
│   ├── data_loader.py           # لودر JSON
│   ├── stats.py                 # آمار (holm، welch، mean_ci)
│   ├── probes.py                # توابع تشخیص نشانه
│   ├── data.py                  # ساخت داده (از نوت‌بوک)
│   ├── models.py                # مدل‌ها (از نوت‌بوک)
│   ├── reproduce_*.py           # اسکریپت‌های بازتولید
│   └── reproduce_all_tables.py  # اجرای همه
│
├── results/                     # CNN3 (مقاله اصلی)
├── results_light/               # CNN2
├── results_10color/             # ۱۰ رنگ
├── results_mlp_rho09/           # MLP ρ=0.9
├── results_mlp_rho99/           # MLP ρ=0.99
├── results_rho099/              # CNN3 ρ=0.99
├── results_waterbirds/          # Waterbirds
├── results_minimal/             # نسخه حداقلی
├── results_paper/               # آزمایش‌های تکمیلی
│
└── models/                      # مدل‌های ذخیره‌شده (اختیاری)
```

---

## ⚠️ محدودیت‌ها و هشدارها

### ۱. جدول ۱-ب (توزیع رنگ)

فایل `raw_results_5seed.json` فقط دقت‌ها را دارد، نه تعداد نمونه‌ها. برای بازتولید کامل جدول ۱-ب، باید یا نوت‌بوک را دوباره اجرا کنی و تعدادها را ذخیره کنی، یا جدول ۱-ب را از مقاله حذف کنی.

### ۲. جدول ۶ و ۱۰ (Counterfactual)

این جدول‌ها به مدل‌های آموزش‌دیده نیاز دارند (`models/*.pth`). اگر مدل‌ها ذخیره نشده‌اند، این جدول‌ها فقط با اجرای مجدد نوت‌بوک قابل بازتولید هستند.

### ۳. تعداد seed

- CNN3، CNN2، MLP، Waterbirds: ۵ seed (یا ۳ برای مقایسه روش‌ها)
- ۱۰ رنگ: ۳ seed

با n=۳ (یا ۵)، توان آزمون‌های آماری پایین است. نتایج به‌عنوان **شواهد اولیه** گزارش می‌شوند، نه اثبات قطعی.

### ۴. تنظیمات محدود

- Waterbirds: ۱۵ epoch (در برابر ۳۰۰ epoch مقاله اصلی) و هایپرپارامترهای تنظیم‌نشده
- IRM روی Waterbirds اجرا نشده
- هایپرپارامترهای پنج روش تنظیم نشده‌اند

**بنابراین، مقایسه روش‌ها در این مقاله یک مطالعه مقدماتی است، نه یک مقایسه نهایی و منصفانه.**

---

## 🔧 وابستگی‌ها

`requirements.txt`:

```
torch>=2.0.0
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0
matplotlib>=3.7.0
scikit-learn>=1.2.0
```

---

## 📖 ارجاع

اگر از این کد یا داده استفاده می‌کنی، لطفاً به مقاله ارجاع بده:

```
Zarean, K. (2025). Spurious Correlations in Colored MNIST and Waterbirds:
A Comprehensive Experimental Study. [Journal/Conference].
```

---

## 📧 تماس

برای سوال یا گزارش مشکل، از طریق GitHub Issues یا ایمیل:

**[your-email@example.com]**

---

## 📜 مجوز

MIT License — see `LICENSE` file.
