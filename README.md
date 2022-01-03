# Folder: keras-retinanet
Berisi model implementasi RetinaNet dengan menggunakan **Keras** dan **Tensorflow**. Menerima dataset berupa gambar (.jpg) beserta labelnya (.xml) dan menghasilkan file *output* berupa model yang dapat digunakan untuk mendeteksi objek pada gambar lain.
Perintah untuk melakukan *train* model:
```shell
python keras_retinanet/bin/train.py --random-transform --image-max-side [ukuran maksimum gambar] --compute-val-loss --epoch [jumlah epoch] --tensorboard-dir [path output tensorboard] --snapshot-path [path output model] pascal [folder dataset]
```

# Folder: Utilities
Berisi modul-modul **Python** yang digunakan untuk melakukan pemrosesan data. Rincian tiap file:
#### `batch_rename.py` 
Untuk mengganti nama banyak file dalam satu folder secara bersamaan. Menerima argumen: lokasi file, tipe file, dan nama file yang hasil penggantian nama. Nama file hasil rename akan dimulai dari 1 sesuai dengan urutan kemunculan file.
```shell
python batch_rename.py --dir [path berisi file] --ext [tipe file] --name [nama file hasil rename]
```
#### `make_dataset.py` 
Untuk membagi data menjadi *train* dan *validation*. Menghasilkan tiga buah file .txt: 
  - `train.txt`: berisi nama *file* yang digunakan untuk *train*
  - `val.txt`: berisi nama *file* yang digunakan untuk *validation* (*test*)
  - `trainval.txt`: berisi seluruh nama *file*.
Menerima argumen: lokasi file, tipe file, dan ratio *train* dan *validation* yang didefinisikan dengan persentase untuk data *train*.
```shell
python make_dataset.py --dir [path berisi file] --ext [tipe file] --ratio [persentase data train]
```
#### `detect_image.py` 
Untuk mendeteksi objek pada gambar masukkan dengan menggunakan model yang sudah dihasilkan. Sudah diimplementasi pada PL.
#### `xml_processing.py` 
Untuk menghitung jumlah tiap kelas pada label di dataset (file .xml). Menghasilkan file csv berisi jumlah kelas untuk tiap file label xml. Menerima argumen: lokasi file xml, dan nama file csv yang dihasilkan (default: class_count.csv).
```shell
python xml_processing.py --dir [path file xml] --name [nama file csv yang dihasilkan]
```
