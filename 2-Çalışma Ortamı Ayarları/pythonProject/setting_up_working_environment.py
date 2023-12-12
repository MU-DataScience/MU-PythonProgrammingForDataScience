#################################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
#################################################
print("Hello World")

print("Hello AI Era")

print(9)
9.2

type(9)
type(9.2)
type("Mrb")

#################################################
# Atamalar ve Değişkenler (Assignments & Variables)
#################################################

a = 9
b = "hello ai era"
b

c = 10

a * c

a * 10

a - c

d = a - c


#################################################
# Virtual Environment (Sanal Ortam) ve Package Management (Paket Yönetimi)
#################################################

# Sanal Ortamların Listelenmesi
# conda env list

# Sanal Ortam Oluşturma
# conda create -n myenv

# Sanal Ortamı aktif etme
# conda activate my_env

# Sanal Ortamı deaktif etme
# conda deactivate

# yüklü paketlerin listelenmesi
# conda list

# paket yükleme
# conda install numpy

# aynı anda birden fazla paket yükleme
# conda install numpy scipy pandas

# paket silme
# conda remove numpy

# Belirli bir versiyona göre paket yükleme
# conda install numpy=1.20.1

# Paket yükseltme
# conda upgrade conda

# Tüm paketlerin yükseltilmesi:
# conda upgrade -all

# pip: pypi (python package index) paket yönetim aracı

# paket yükleme
# pip install pandas

# paket yükleme versiyona göre
# pip install pandas==1.2.1

# Tüm paketlerin versiyonlarını aktarma
# conda env export > environment.yaml