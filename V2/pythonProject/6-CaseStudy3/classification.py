import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option("display.float_format", lambda x: '%.2f' % x)

# region Görev 1
# Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_excel("6-CaseStudy3/gezinomi_tanitim/miuul_gezinomi.xlsx")
df.head()
df.shape
df.info()
# Soru2: Kaç unique şehir vardır? Frekanslarınedir?
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# Soru3:Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df.groupby("ConceptName").agg({"ConceptName": "count"})

# Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Soru9: Şehir-Concept kırılımındaPRICE ortalamalarınedir?
df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"})
# endregion
# region Görev 2 SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.
# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max() + 1],
                        labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"])
# endregion
# region Görev 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz.


df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})
# endregion
# region Görev 4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
# Elde ettiğiniz çıktıyı agg_df olarak kaydediniz.
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price",
                                                                                                   ascending=False)
agg_df.head(20)
# endregion
# region Görev 5: Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df.reset_index(inplace=True)
agg_df.head()
# endregion
# region Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: sales_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir.

agg_df["sales_level_based"] = ["_".join([city.upper(), concept.upper(), season.upper()])
                               for city, concept, season in zip(agg_df["SaleCityName"],
                                                                agg_df["ConceptName"],
                                                                agg_df["Seasons"])]

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(),
                                                                                     axis=1)
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

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]

new_user2 = "GIRNE_YARIM PANSIYON_LOW"
agg_df[agg_df["sales_level_based"] == new_user2]["SEGMENT"]
# endregion
