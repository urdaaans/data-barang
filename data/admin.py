from django.contrib import admin
from .models import DataBarang, DataBarangKeluar
# Register your models here.
admin.site.site_title= "Data Barang"
admin.site.site_header = "Data Barang"
admin.site.register(DataBarang)
admin.site.register(DataBarangKeluar)