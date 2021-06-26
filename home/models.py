from django.db import models
from PIL import Image
from django.db.models.base import Model
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime, timedelta
import datetime

from crequest.middleware import CrequestMiddleware
from django.conf import settings
from django.core.files.storage import FileSystemStorage

    
class BukuCategory(models.Model):
    buku_category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.buku_category
    
class Buku(models.Model):
    kode_buku = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255,null=True, blank=True)
    tahun_terbit = models.DateField(null=True, blank=True)
    judul_buku = models.CharField(max_length=255)
    cover_pic = models.ImageField( null=True ,blank=True, upload_to="images", default='python.jpg')
    document = models.FileField(upload_to='pdf',null=True ,blank=True)
    buku_category = models.ForeignKey(BukuCategory, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    updated       = models.DateField(auto_now=True)
    published     = models.DateTimeField(auto_now_add=True)
    slug          = models.SlugField(unique=True,editable=False)
    
    def __str__(self):
        return self.kode_buku +" "+self.judul_buku
    
    def save(self):
        self.slug = slugify(self.judul_buku)
        super().save()
        img = Image.open(self.cover_pic.path)
        fs = FileSystemStorage()
        uploaded_file_url = self.document.path
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            
            
    def get_absolute_url(self):
        return reverse('home')
        
    
class PinjamBuku(models.Model):   
    peminjam_nama = models.ForeignKey(User, on_delete=models.CASCADE)
    kd_buku = models.ForeignKey(Buku, null=True,blank=True, on_delete=models.CASCADE)
    judul_buku = models.CharField(max_length=255)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_berakhir = models.DateField(default=f'{datetime.datetime.now().date()+timedelta(days=7)}',null=True, blank=True)
    
    # def get_absolute_url(self):
    #     return reverse('home')
    # def save(self, *args, **kwargs):
    #     current_request = CrequestMiddleware.get_request()
    #     user = current_request.user.id
    #     userr_id = str(current_request.user.username)
    #     userss = User.objects.get(id=user)
    #     bukuss = Buku.objects.get(kode_buku="0001")

        
            
    #     self.peminjam_nama = userss
    #     self.kd_buku = bukuss
    #     # self.judul = "hello"
    #     self.tanggal_berakhir = datetime.datetime.now().date()+timedelta(days=7)
    #     return super().save(*args, **kwargs)
        
    # def get_absolute_url(self):
    #     # return reverse('article-detail', args= (str(self.id)))
    #     return reverse('pinjam/rak.html')
        
        
        
        
        
    
    
    
    