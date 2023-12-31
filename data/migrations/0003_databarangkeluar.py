# Generated by Django 5.0 on 2023-12-20 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_databarang_tanggal_ditambah'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBarangKeluar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jumlah_keluar', models.IntegerField(default=0)),
                ('tanggal_keluar', models.DateField()),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.databarang')),
            ],
        ),
    ]
