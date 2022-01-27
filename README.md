# Twitter üzerinden gerçek zamanlı akan veri üzerinden SparkSQL ile sorgu

## 1. Docker imajının kurulması

Bu imajın kurulumu için bilgisayarınızda Docker'ın kurulu olması gerekmektedir. Linux ve Mac'te ek işlem gerekmezken Windows için Docker yüklemeden önce Windows Subsystem For Linux (WSL) yüklenmesi gerekmektedir.

[WSL Kurulumu](https://docs.microsoft.com/en-us/windows/wsl/install)

[Docker Kurulumu](https://www.docker.com/get-started)

Docker kurulduktan sonra bu repository sağ üstten ister zip olarak ister terminalden git clone komutuyla lokale indirilir.

    git clone https://github.com/tarikyasar/inf-438

### a. Twitter API'ının çalıştırılması

Bu kod repository'si ile birlikte verilen <strong>tweet.py</strong> dosyasını çalıştırmak için öncelikle Twitter'dan API anahtarının alınması gerekmektedir.

Anahtar [buradan](https://developer.twitter.com/en/docs/twitter-api) alınabilir. Alınma adımları ek olarak bu repository'de bulunan rapor dosyasında bulunabilir.

Anahtar alındıktan sonra bu repository'de bulunan <strong>tweet.py</strong> dosyası herhangi bir text editor ile açılır ve içinde bulunan <em>bearer_token</em> değişkenine bu API anahtarı atanır.

Klasörün içindeyken aşağıdaki terminal komutuyla Docker imajı kurulur.

    docker build . -t ornek-isim:latest

Komut çalıştırıldıktan sonra Docker uygulaması açılır. Images sekmesinde Docker imajının oluşturulduğu görülür.

![Screenshot 1](/screenshots/ss_1.png)

Üzerinde gelindiğinde çıkan Run tuşuna basarak container oluşturulur.

![Screenshot 2](/screenshots/ss_2.png)

Çıkan pencerede container'a istenirse bir isim verilebilir. Verilmezse rastgele bir isim atanır. Bu örnekte "ornek-container-ismi" verilmiştir.

![Screenshot 3](/screenshots/ss_3.png)

Containers/Apps sekmesine gidildiğinde container'ın oluşturulduğu gözlemlenir. İlgili container'ın üzerinde gelince çıkan "CLI" butonuna basılarak terminal üzerinden container çalıştırılır.

![Screenshot 4](/screenshots/ss_4.png)

![Screenshot 5](/screenshots/ss_5.png)

## 2. Kafka'nın çalıştırılması

Docker container'ı çalıştırıldıktan sonra aşağıdaki komut çalıştırılarak Kafka, Zookeeper ve Kafka Consumer çalıştırılır.

    cd /home/Twitter
    bash run_kafka.sh

## 3. Twitter API

İkinci adım gerçekleştirildikten sonra Docker'ın uygulamasından bir terminal penceresi daha açılır. Burada da aşağıdaki komutlar çalıştırılarak Twitter API'ı çalıştırılıp sonuçlar ilk açılan terminal penceresinden gözlemlenebilir.

Komut kullanımında argüman olarak görüntülenmek istenen topic girilmelidir. Twitter gündeminde olanlardan biri seçilebililir.
Örnek: #karyagisi için

    python3 tweet.py karyagisi

    cd /home/Twitter
    python3 tweet.py trend
