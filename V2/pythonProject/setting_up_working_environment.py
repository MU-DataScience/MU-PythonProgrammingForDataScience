#######################################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
#######################################################
print("Hello World")
print("Hello AI Era")

print(9)
9.2

type(9)
type(9.2)

type("Mrb")

#######################################################
# Atamalar ve Değişkenler (Assignments & Variables)
#######################################################

a = 9
a

b = "hello ai era"
b

c = 10

a * c

a * 10

d = a - c


#######################################################
# Virtual Environment (Sanal Ortam) ve Paket Yönetimi (Package Management)
#######################################################

# Sanal Ortamların Listenlenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create -n myenv

# Sanal ortamı aktif etme:
# conda activate my_env

# Sanal ortamı deaktif etme:
# conda deactivate my_env

# Yüklü paketlerin listelenmesi:
# conda list

# Paket Yükleme:
# conda install numpy

# Aynı anda birden fazla Paket Yükleme:
# conda install numpy scipy pandas

# Paket Silme:
# conda remove numpy

# Belirli bir versiyone göre Paket Yükleme:
# conda install numpy=1.20.1

# Paket Yükseltme:
# conda upgrade conda

# Tüm Paketlerin Yükseltilmesi:
# conda upgrade --all

# pip pypi(python package index) paket yönetim aracı

# Paket Yükleme
# pip install pandas

# Paket Yükleme versiyona göre
# pip install pandas==1.2.1

# Paketleri yaml dosyanına gönderme
# conda env export > environment.yaml

# Yaml dosyasına göre environment oluşturma
# conda env create -f environment.yaml -n my_env
