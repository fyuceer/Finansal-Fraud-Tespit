# 📈 Finansal Fraud Tespit Sistemi

Python ve makine öğrenmesi kullanılarak finansal işlemlerde dolandırıcılık (fraud) tespiti gerçekleştiren bir sınıflandırma projesidir. Projede farklı makine öğrenmesi algoritmaları aynı veri seti üzerinde eğitilerek performansları karşılaştırılmış ve finansal dolandırıcılık tespiti açısından en başarılı model belirlenmiştir.

Finansal işlemlerde gerçekleştirilen sahte veya şüpheli işlemlerin otomatik olarak tespit edilmesi, finansal güvenliğin sağlanması açısından önemli bir problemdir.

Bu projede **PaySim** veri seti kullanılarak işlemlerin dolandırıcılık içerip içermediği tahmin edilmektedir.

Projenin temel amacı;

- Finansal işlem verilerini analiz etmek,
- Dolandırıcılık içeren işlemleri tespit etmek,
- Farklı makine öğrenmesi algoritmalarını karşılaştırmak,
- Fraud tespiti açısından en başarılı modeli belirlemektir.

##  Kullanılan Makine Öğrenmesi Modelleri

Projede üç farklı sınıflandırma algoritması kullanılmıştır:

- **Logistic Regression**
- **Random Forest**
- **Naive Bayes**

Modeller aynı eğitim ve test veri setleri üzerinde değerlendirilerek karşılaştırılmıştır.

##  Kullanılan Özellikler

Model eğitiminde aşağıdaki işlem özellikleri kullanılmıştır:

- `step`
- `amount`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`

Hedef değişken:

- `isFraud`

`isFraud` değişkeni işlemin dolandırıcılık içerip içermediğini belirtmektedir.

- `0` → Normal işlem
- `1` → Dolandırıcılık içeren işlem

##  Model Sonuçları

Modeller Accuracy, Precision, Recall ve F1-Score metrikleri kullanılarak değerlendirilmiştir.

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | %99.92 | %88.32 | %46.96 | %61.31 |
| Random Forest | **%99.96** | **%95.70** | **%70.37** | **%81.10** |
| Naive Bayes | %99.21 | %2.91 | %15.91 | %4.93 |

###  En Başarılı Model

Yapılan karşılaştırma sonucunda **Random Forest** modeli en başarılı sonuçları vermiştir.

Random Forest modeli:

- **Accuracy:** %99.96
- **Precision:** %95.70
- **Recall:** %70.37
- **F1-Score:** %81.10

özelliklerini elde etmiştir.

Dolandırıcılık tespitinde yalnızca Accuracy değerine bakmak yeterli değildir. Özellikle dolandırıcılık gibi sınıfların dengesiz olduğu veri setlerinde **Precision, Recall ve F1-Score** değerleri model performansının değerlendirilmesinde daha anlamlı sonuçlar sunmaktadır.

Bu nedenle yapılan karşılaştırmada Random Forest modeli öne çıkmıştır.

##  Veri Seti

Projede **PaySim** finansal işlem veri seti kullanılmıştır.

Veri seti çok büyük olduğu için CSV dosyası GitHub repository'sine dahil edilmemiştir. GitHub'ın standart dosya yükleme sınırı nedeniyle veri setinin tamamı repository içerisinde tutulmamaktadır.

Projeyi çalıştırmak için PaySim veri setinin indirilmesi ve aşağıdaki dosya adının proje klasörüne eklenmesi gerekmektedir:

```text
PS_20174392719_1491204439457_log.csv
```

##  Proje Yapısı

```text
Finansal-Fraud-Tespit/
│
├── fraud_detection.py
├── requirements.txt
└── .gitignore
```

##  Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Scikit-learn

##  Kullanılan Modeller

- Logistic Regression
- Random Forest
- Naive Bayes

##  Geliştirici

**FeyzaSultanYüceer**
