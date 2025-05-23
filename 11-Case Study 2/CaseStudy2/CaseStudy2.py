# region List Comprehension
# region Görev 1
# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NUM_" + col.upper() if df[col].dtypes != 'O' else col.upper() for col in df.columns]

# endregion
# region Görev 2
# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df.info()

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# endregion
# region Görev 3
# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df.info()
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]
new_df.head()
# endregion
# endregion
# region Pandas Alıştırmalar

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.shape

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
df["pclass"].unique()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[["pclass", "parch"]].nunique()

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtypes
df.info()

# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.
import pandas as pd

pd.set_option('display.width', 500)
df[df["embarked"] == "C"]

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] != "S"]

df[df["embarked"] != "S"]["embarked"].unique()

df[~(df["embarked"] == "S")]["embarked"].unique()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df["age"] < 30) & (df["sex"] == "female")]

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz
df[(df["fare"] > 500) | (df["age"] > 70)]

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop(["who"], axis=1, inplace=True)

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df = sns.load_dataset("titanic")
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})


# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz. (apply ve lambda yapılarını kullanınız)

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)

df["age_flag"] = df["age"].apply(age_30)
df.columns

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")
df.head()
df.shape

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.info()
df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
df.head()
df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day").agg({"total_bill": ["min", "max", "mean"],
                                                                          "tip": ["min", "max", "mean"]})

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
new_df = df.sort_values(by=["total_bill_tip_sum"], ascending=False).head(30)
new_df.shape
# endregion
