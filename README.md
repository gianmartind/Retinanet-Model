# Folder: keras-retinanet
Berisi model implementasi RetinaNet dengan menggunakan **Keras** dan **Tensorflow**. Menerima dataset berupa gambar (.jpg) beserta labelnya (.xml) dan menghasilkan file *output* berupa model yang dapat digunakan untuk mendeteksi objek pada gambar lain.
Perintah untuk melakukan *train* model:
```shell
python keras_retinanet/bin/train.py --random-transform --image-max-side [ukuran maksimum gambar] --compute-val-loss --epoch [jumlah epoch] --tensorboard-dir [path output tensorboard] --snapshot-path [path output model] pascal [folder dataset]
```

# Folder: Utilities
Berisi modul-modul **python** yang digunakan untuk melakukan pemrosesan data. Rincian tiap file:
- `batch_rename.py`: Untuk mengganti nama banyak file dalam satu folder secara bersamaan.
```shell
python batch_rename.py --dir [path berisi file] --ext [tipe file] --name [nama file hasil rename]
```
- `make_dataset.py`: Untuk membagi data menjadi *train* dan *validation*. Menghasilkan tiga buah file .txt: 
  - `train.txt`: berisi nama *file* yang digunakan untuk *train*
  - `val.txt`: berisi nama *file* yang digunakan untuk *validation* (*test*)
  - `trainval.txt`: berisi seluruh nama *file*
```shell
python make_dataset.py --dir [path berisi file] --ext [tipe file] --
```
- `detect_image.py`: Untuk mendeteksi objek pada gambar masukkan dengan menggunakan model yang sudah dihasilkan. Sudah diimplementasi pada PL.
- `xml_processing.py`: Untuk menghitung jumlah tiap kelas pada label di dataset (file .xml).
