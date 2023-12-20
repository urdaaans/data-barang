# Generated by Django 5.0 on 2023-12-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBarang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_barang', models.CharField(max_length=200)),
                ('tanggal_ditambah', models.DateField(auto_now_add=True)),
                ('stok', models.IntegerField(default=0)),
            ],
        ),
    ]