# Spurious Correlations in Colored MNIST and Waterbirds

**A Comprehensive Empirical Study on Detecting and Mitigating Spurious Correlations in Image Classification**

**نویسنده:** کوثر زارعان

**مقاله:** تشخیص و کاهش همبستگی‌های کاذب در طبقه‌بندی تصاویر: یک مطالعه تجربی جامع روی Colored MNIST و Waterbirds

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

##  خلاصه

این مخزن شامل کد، داده خام، و اسکریپت‌های بازتولید مقاله است. همه اعداد، جدول‌ها و شکل‌های مقاله از فایل‌های `results/*/results.json` بازتولید می‌شوند.

** توجه:** این مقاله یک **مطالعه تجربی** است، نه معرفی روش جدید. سهم آن مقایسه نظام‌مند پنج روش کاهش سوگیری در طیف ρ و دو طراحی Colored MNIST است.

---

##  ساختار مخزن

```
spurious-correlations-colormnist-waterbirds/
├── README.md                          # این فایل
├── REPRODUCIBILITY_REPORT.md          # نگاشت مقاله → JSON → نوت‌بوک
├── CITATION.cff
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── notebooks/                         # نوت‌بوک‌های Colab
│   ├── README.md
│   ├── colored_mnist_project.ipynb     (CNN3، ρ=0.9، ۳ seed)
│   ├── colored_mnist_10colors.ipynb    (نسخه ۱۰ رنگ)
│   ├── paper_experiments.ipynb         (جاروب ۵ seed)
│   ├── colored_mnist_mlp_rho09.ipynb   (MLP، ρ=0.9)
│   ├── colored_mnist_mlp_rho99.ipynb   (MLP، ρ=0.99)
│   ├── colored_mnist_minimal.ipynb     (CNN1، ρ=0.9)
│   ├── colored_mnist_light.ipynb       (CNN2، ρ=0.9)
│   ├── colored_mnist_rho099.ipynb      (CNN3، ρ=0.99)
│   └── waterbirds_experiment.ipynb     (Waterbirds)
│
├── results/                           # داده خام (JSON)
│   ├── project_results/results.json             (CNN3، ρ=0.9)
│   ├── results_10colors/results.json            (نسخه ۱۰ رنگ)
│   ├── paper_results/results.json               (جاروب ۵ seed)
│   ├── project_mlp_rho09/results.json           (MLP، ρ=0.9)
│   ├── project_mlp_rho99/results.json           (MLP، ρ=0.99)
│   ├── project_minimal_results/results.json     (CNN1، ρ=0.9)
│   ├── project_light_results/results.json       (CNN2، ρ=0.9)
│   ├── project_rho099_results/results.json      (CNN3، ρ=0.99)
│   └── results_waterbirds/raw_results.json      (Waterbirds)
│
├── figures/                           # شکل‌های مقاله
│   ├── fig0_dataset_samples.png
│   ├── fig1_baseline_training_curves.png
│   ├── fig3_saliency.png
│   ├── fig4_gradcam.png
│   ├── fig_acc_vs_rho.png
│   ├── fig_drop_vs_rho.png
│   ├── fig_dropout.png
│   ├── fig_color_effect.png
│   ├── fig_theory_check.png
│   ├── fig_confusion_ood2.png
│   ├── fig_integrated_gradients.png
│   ├── fig5_methods_comparison.png
│   └── fig6_training_dynamics.png
│
└── src/                               # کد بازتولید
    ├── README.md
    ├── reproduce_all_tables.py
    ├── reproduce_table1b.py
    ├── reproduce_table7.py
    └── stats.py
```

---

##  نگاشت نوت‌بوک‌ها به جدول‌های مقاله

| # | نوت‌بوک | معماری / نسخه | خروجی JSON | جدول‌های مقاله | شکل‌های مقاله |
|---|---|---|---|---|---|
| ۱ | `colored_mnist_project.ipynb` | **CNN3** (مقاله اصلی) | `results/project_results/results.json` | **۲، ۳، ۴، ۹، ۱۰** | **۲، ۳، ۴** |
| ۲ | `colored_mnist_10colors.ipynb` | **نسخه ۱۰ رنگ** | `results/results_10colors/results.json` | **۱۳، ۱۵** | — |
| ۳ | `paper_experiments.ipynb` | **MLP/CNN3، جاروب ۵ seed** | `results/paper_results/results.json` | **۵، ۶، ۷، ۸** | **۵، ۶، ۷، ۸، ۹، ۱۰، ۱۱** |
| ۴ | `colored_mnist_mlp_rho09.ipynb` | **MLP، ρ=0.9** | `results/project_mlp_rho09/results.json` | ۱۱ (ستون MLP ρ=0.9) | — |
| ۵ | `colored_mnist_mlp_rho99.ipynb` | **MLP، ρ=0.99** | `results/project_mlp_rho99/results.json` | ۱۱ (ستون MLP ρ=0.99) | — |
| ۶ | `colored_mnist_minimal.ipynb` | **CNN1، ρ=0.9** | `results/project_minimal_results/results.json` | ۱۱ (ستون CNN1) | — |
| ۷ | `colored_mnist_light.ipynb` | **CNN2، ρ=0.9** | `results/project_light_results/results.json` | ۱۱ (ستون CNN2) | — |
| ۸ | `colored_mnist_rho099.ipynb` | **CNN3، ρ=0.99** | `results/project_rho099_results/results.json` | ۱۱ (ستون CNN3 ρ=0.99) | — |
| ۹ | `waterbirds_experiment.ipynb` | **Waterbirds** | `results/results_waterbirds/raw_results.json` | **۱۲** | — |

### توضیح جدول‌ها

| جدول | محتوا | نوت‌بوک منبع | اسکریپت بازتولید |
|---|---|---|---|
| جدول ۱-ب | توزیع رنگ/برچسب | (از داده خام) | `src/reproduce_table1b.py` |
| جدول ۲ | ارزیابی مدل پایه | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۳ | Counterfactual | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۴ | Misspecification | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۵ | دقت ID/OOD/شکاف | `paper_experiments.ipynb` (+ `project_*`) | `src/reproduce_all_tables.py` |
| جدول ۶ | اثر Dropout | `paper_experiments.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۷ | اتحاد و MAE | `paper_experiments.ipynb` | `src/reproduce_table7.py` |
| جدول ۸ | خطای هر رقم | `paper_experiments.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۹ | روش‌ها (دورنگ) | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۱۰ | پروفایل رنگ (دورنگ) | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۱۱ | مقایسه روش‌ها × معماری | (تلفیق ۶ نوت‌بوک) | `src/reproduce_all_tables.py` |
| جدول ۱۲ | Waterbirds | `waterbirds_experiment.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۱۳ | روش‌ها (۱۰ رنگ) | `colored_mnist_10colors.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۱۴ | مقایسه دو طراحی | (تلفیق ۹ و ۱۳) | `src/reproduce_all_tables.py` |
| جدول ۱۵ | پروفایل رنگ (۱۰ رنگ) | `colored_mnist_10colors.ipynb` | `src/reproduce_all_tables.py` |
| جدول ۱۶ | مقایسه با کارهای پیشین | (دستی) | (در مقاله ثابت) |

---

##  نصب و اجرا

### پیش‌نیازها

- Python 3.10+
- pip

### نصب

```bash
git clone https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds.git
cd spurious-correlations-colormnist-waterbirds
pip install -r requirements.txt
```

### بازتولید همه جدول‌ها

```bash
python src/reproduce_all_tables.py
python src/stats.py
python src/reproduce_table1b.py
python src/reproduce_table7.py
```

### بازتولید یک جدول خاص

```bash
# جدول ۱-ب (توزیع رنگ/برچسب)
python src/reproduce_table1b.py

# جدول ۷ (اتحاد و MAE)
python src/reproduce_table7.py

# p-value و Cohen's d (Waterbirds)
python src/stats.py

# همه جدول‌های دیگر
python src/reproduce_all_tables.py
```

### بازتولید از نوت‌بوک

اگر می‌خواهی از صفر بازتولید کنی:

1. هر نوت‌بوک را در Colab باز کن (Runtime → GPU)
2. همه سلول‌ها را اجرا کن (Run all)
3. فایل `results.json` را در پوشه مربوطه ذخیره کن
4. اسکریپت بازتولید را اجرا کن

**زمان تقریبی اجرای کامل روی T4 GPU:** ۴۰–۶۰ دقیقه برای هر نوت‌بوک.

---

##  داده خام

همه فایل‌های JSON خام در پوشه‌های `results/*/` قرار دارند:

| فایل | توضیح | تعداد seed |
|---|---|---|
| `results/project_results/results.json` | CNN3، ρ=0.9 | ۳ |
| `results/results_10colors/results.json` | نسخه ۱۰ رنگ | ۳ |
| `results/paper_results/results.json` | جاروب MLP/CNN3 | ۵ |
| `results/project_mlp_rho09/results.json` | MLP، ρ=0.9 | ۳ |
| `results/project_mlp_rho99/results.json` | MLP، ρ=0.99 | ۳ |
| `results/project_minimal_results/results.json` | CNN1، ρ=0.9 | ۳ |
| `results/project_light_results/results.json` | CNN2، ρ=0.9 | ۳ |
| `results/project_rho099_results/results.json` | CNN3، ρ=0.99 | ۳ |
| `results/results_waterbirds/raw_results.json` | Waterbirds | ۳ |

### ساختار JSON

برای `paper_results/results.json`، کلیدها به شکل `"{arch}|{rho}|{dropout}|{seed}"` هستند:

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
    "conf_ood2": [[968, 0, 1, "..."]]
  }
}
```

برای `project_results/results.json` و `results_10colors/results.json`، ساختار متفاوت است:

```json
{
  "cfg": {},
  "RES": {
    "Baseline": {
      "0": {"train": "...", "val": "...", "id": "...", "ood1": "...", "ood2": "..."}
    }
  },
  "CUE": {
    "Baseline": {
      "0": {"original": {}, "A_swap": {}}
    }
  }
}
```

مقادیر دقت در بازه ۰–۱ هستند (ضرب در ۱۰۰ برای درصد).

---

##  محدودیت‌ها

### ۱. جدول ۱-ب (توزیع رنگ)

`src/reproduce_table1b.py` این جدول را از داده خام MNIST بازتولید می‌کند. **نیازی به اجرای مجدد نوت‌بوک نیست.**

### ۲. جدول ۳ و ۴ (Counterfactual و Misspecification)

این جدول‌ها به مدل‌های آموزش‌دیده نیاز دارند. اگر مدل‌ها ذخیره نشده‌اند (`models/*.pth` در `.gitignore` است)، این جدول‌ها فقط با اجرای مجدد نوت‌بوک قابل بازتولید هستند. **پیشنهاد:** مدل‌ها را در GitHub Release آپلود کن، نه در git.

### ۳. تعداد seed

- CNN3، CNN2، MLP، Waterbirds: ۳ یا ۵ seed (بسته به فایل)
- ۱۰ رنگ: ۳ seed

با n=۳ (یا ۵)، توان آزمون‌های آماری پایین است. نتایج به‌عنوان **شواهد اولیه** گزارش می‌شوند، نه اثبات قطعی.

### ۴. تنظیمات محدود

- Waterbirds: ۱۵ epoch (در برابر ۳۰۰ epoch مقاله اصلی) و هایپرپارامترهای تنظیم‌نشده
- IRM روی Waterbirds اجرا نشده
- هایپرپارامترهای پنج روش تنظیم نشده‌اند

**بنابراین، مقایسه روش‌ها در این مقاله یک مطالعه مقدماتی است، نه یک مقایسه نهایی و منصفانه.**

---

##  وابستگی‌ها

`requirements.txt`:

```
torch>=2.0.0
torchvision>=0.15.0
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0
matplotlib>=3.7.0
scikit-learn>=1.2.0
jupyter>=1.0.0
```

---

##  ارجاع

اگر از این کد یا داده استفاده می‌کنی، لطفاً به مقاله ارجاع بده:

```bibtex
@article{zarean2026spurious,
  title   = {Spurious Correlations in Colored MNIST and Waterbirds:
             A Comprehensive Empirical Study},
  author  = {Zarean, Kosar},
  year    = {2026},
  url     = {https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds}
}
```

---

##  تماس

برای سوال یا گزارش مشکل، از طریق GitHub Issues:

https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds/issues

---

##  مجوز

MIT License — see [`LICENSE`](LICENSE).
