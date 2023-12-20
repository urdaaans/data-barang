from django.db import models
from django.core.exceptions import ValidationError

class DataBarang(models.Model):
    id = models.AutoField(primary_key=True)
    nama_barang = models.CharField(max_length=200)
    tanggal_ditambah = models.DateField()
    stok = models.IntegerField(default=0)

    def __str__(self):
        formatted_date = self.tanggal_ditambah.strftime("%d/ %m/ %Y")
        return "{} : {}".format(self.nama_barang, formatted_date)

class DataBarangKeluar(models.Model):
    id = models.AutoField(primary_key=True)
    barang = models.ForeignKey(DataBarang, on_delete=models.CASCADE)
    jumlah_keluar = models.IntegerField(default=0)
    tanggal_keluar = models.DateField()

    def clean(self):
        # Validate that the quantity to be taken out is not greater than the available stock
        if self.jumlah_keluar > self.barang.stok:
            raise ValidationError('Jumlah barang keluar tidak boleh melebihi stok yang tersedia.')

    def save(self, *args, **kwargs):
        # Update the stock when saving the DataBarangKeluar instance
        self.barang.stok -= self.jumlah_keluar
        self.barang.save()
        super().save(*args, **kwargs)

    def __str__(self):
        formatted_date = self.tanggal_keluar.strftime("%d/ %m/ %Y")
        return "{}: {} keluar pada {}".format(self.barang.nama_barang, self.jumlah_keluar, formatted_date)
