from django.urls import path
from .views import PinjamDetailView, AddPinjamView, RakView,pdf_viwes,CreatePinjamView, RiwayatView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('category/<str:cats>/', CategoryView, name='pinjam-category'),
    path('pinjam/<slug:slug>/', PinjamDetailView.as_view(), name='pinjam-detail'),
    path('add_pinjam/<int:pk>/', AddPinjamView, name='pinjam-add' ),
    # path('add_pinjam/<int:pk>/', AddPinjamView.as_view(), name='pinjam-add' ),
    path('rak/',RakView.as_view(), name='pinjam-rak' ),    
    path('view_pdf/<pk>', pdf_viwes,name='pdf'),
    path('Create_pinjam/<pk>', CreatePinjamView, name='create-pinjam'),
    path('riwayat/', RiwayatView.as_view(), name='riwayat'),

    
   
    # path('add/<pk>/', add_buku, name='add_buku')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


