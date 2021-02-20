from django.db import models
from autoslug import AutoSlugField
class KategoriModel(models.Model):
    isim = models.CharField(max_length=40, blank=False, null=False)
    slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:              
        db_table= "kategori"                     #tablo ismini manuel girmek için
        verbose_name_plural = "Kategoriler"      #admin panelde görünecek model ismi
        #verbose_name = "Kategori"                #admin panelde görünecek tekil model ismi

    def __str__(self):
        return self.isim
