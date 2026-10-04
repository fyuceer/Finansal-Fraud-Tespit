import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# 1. VERİ SETİNİ YÜKLE
# ============================================================

data = pd.read_csv(
    "PS_20174392719_1491204439457_log.csv",
    encoding="Latin1"
)


# ============================================================
# 2. ÖZELLİKLERİ VE HEDEF DEĞİŞKENİ BELİRLE
# ============================================================

X = data[
    [
        "step",
        "amount",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest"
    ]
]

y = data["isFraud"]


# ============================================================
# 3. EĞİTİM VE TEST VERİSİNE AYIR
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ============================================================
# 4. MODELLERİ OLUŞTUR
# ============================================================

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ),
    "Naive Bayes": GaussianNB()
}


# ============================================================
# 5. MODELLERİ EĞİT VE DEĞERLENDİR
# ============================================================

results = []

for model_name, model in models.items():

    print(f"\n{'=' * 50}")
    print(f"{model_name}")
    print(f"{'=' * 50}")

    # Modeli eğit
    model.fit(X_train, y_train)

    # Test verisi üzerinde tahmin
    y_pred = model.predict(X_test)

    # Performans metrikleri
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )
    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )
    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    # Sonuçları kaydet
    results.append({
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1
    })

    # Sonuçları ekrana yazdır
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-Score : {f1:.4f}")


# ============================================================
# 6. MODEL KARŞILAŞTIRMASI
# ============================================================

results_df = pd.DataFrame(results)

print("\n")
print("=" * 70)
print("MODEL KARŞILAŞTIRMASI")
print("=" * 70)

print(results_df.to_string(index=False))