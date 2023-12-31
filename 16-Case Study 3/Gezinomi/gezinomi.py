# region Görev 1: Aşağıdaki Soruları Yanıtlayınız
# Soru 1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz..
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.float_format", lambda x: '%.2f' % x)
pd.set_option("display.width", 500)
df = pd.read_excel("datasets/miuul_gezinomi.xlsx")
df.head()
df.shape
df.info()

# Soru 2: Kaç unique şehir vardır? Frekansları nedir?
df["SaleCityName"].value_counts()
df["SaleCityName"].nunique()

# Soru 3: Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru 4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df["ConceptName"].value_counts()
df.groupby("ConceptName")["ConceptName"].count()

# Soru 5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru 6: Concept türlerine göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru 7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby(by="SaleCityName").agg({"Price": "mean"})

# Soru 8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})

# endregion
# region Görev 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.
# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz.
# - Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz.

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df[pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels).isnull()]["SaleCheckInDayDiff"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

# endregion
# region Görev 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz ?
df.info()

df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})

df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

# endregion
# region Görev 4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
# Elde ettiğiniz çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price",
                                                                                                   ascending=False)
agg_df.head()

# endregion
# region Görev 5: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace=True)

agg_df.head()
# endregion
# region Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: sales_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir.

agg_df["sales_level_based"] = agg_df["SaleCityName"] + "_" + agg_df["ConceptName"] + "_" + agg_df["Seasons"]

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df.head()

# endregion
# region Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni personaları PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])

agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# endregion
# region Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır?
agg_df.sort_values("Price")

new_user = "Antalya_Herşey Dahil_High"
agg_df[agg_df["sales_level_based"] == new_user]

new_user2 = "Girne_Yarım Pansiyon_Low"
agg_df[agg_df["sales_level_based"] == new_user2]
# endregion
