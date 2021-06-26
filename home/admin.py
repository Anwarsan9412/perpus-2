from django.contrib import admin

from .models import   BukuCategory,Buku


admin.site.register(Buku)
# admin.site.register(PinjamBuku)
admin.site.register(BukuCategory)

