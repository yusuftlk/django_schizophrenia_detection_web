from django.db import models
# Create your models here.

class Resoults(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ad')
    surname = models.CharField(max_length=50, verbose_name='Soyad')
    faceDir = models.CharField(max_length=50, verbose_name='Yüz resmi dosya konumu')
    voiceDir = models.CharField(max_length=50, verbose_name='ses dosya konumu')
    faceClass = models.CharField(max_length=10, verbose_name='Yüzüne göre sınıfı')
    voiceClass = models.CharField(max_length=10, verbose_name='Sesine göre sınıfı')
    description = models.TextField(verbose_name='Açıklama')
    date = models.DateField(verbose_name='İşlem Tarihi')
    result = models.TextField(verbose_name='Sonuç')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Adı')
    surname = models.CharField(max_length=50, verbose_name='Soyadı')
    email = models.EmailField(verbose_name='Mail Adresi')
    password = models.CharField(max_length=50, verbose_name='Şifresi')
    username = models.CharField(max_length=50, verbose_name='Kullanıcı Adı')

    def __str__(self):
        return self.name