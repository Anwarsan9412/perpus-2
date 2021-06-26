from django.http import request, response, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.views.generic import TemplateView, DetailView,CreateView,ListView
from home.models import BukuCategory,PinjamBuku,Buku
from django.urls import reverse_lazy, reverse
from home.forms import AddBukuForm
import re
from crequest.middleware import CrequestMiddleware
from django.contrib.auth.models import User
import datetime

from django.template.loader import get_template
from xhtml2pdf import pisa

from django.core.files.storage import  FileSystemStorage


def pdf_viwes(request, *args, **kwargs):
    pk = kwargs.get('pk')
    bukus = Buku.objects.get(id=pk)
    fs = FileSystemStorage()
    # print(bukus.document)
    filename = str(bukus.document)
    if request.user.is_authenticated:
        
        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                # response['Content-Disposition'] = 'filename="pdf/file1.pdf"'
                # response['Content-Disposition'] = 'attachment; filename="file1.pdf"' # browser save
                return response                       
        else:
            return HttpResponseNotFound("The requested pdf was not found in our server.")


# def render_pdf_view(request):
#     template_path = 'pinjam/view_pdf.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # if download
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # if display
#     response['Content-Disposition'] = 'filename="file1.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


# class HomeView(TemplateView):
#     template_name= 'pinjam/home.html'

# def CategoryView(request, cats):
    
#     category_posts = Buku.objects.filter(buku_category=cats)
#     return render(request, 'pinjam/pinjam_category.html', {'cats': cats.title(), 'category_posts': category_posts})
    



class PinjamDetailView(DetailView):
    model = Buku
    template_name = 'pinjam/pinjam_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_buku = BukuCategory.objects.all()
        context = super(PinjamDetailView, self).get_context_data(*args, **kwargs)
        context["cat_buku"] = cat_buku
        # context["urlss"] = self.request.get_full_path()
        return context  

# def add_buku(request, *args, **kwargs):
#     bukus = Buku.objects.get(id=12)
#     pk = kwargs.get('pk')
#     pinjam = get_object_or_404(PinjamBuku, pk=pk)
#     patth = 'file1.pdf'
#     return HttpResponse(patth)

# class AddPinjamView(ListView):
#     model = Buku
#     template_name = 'pinjam/pinjam_add.html'
#     def get_context_data(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         bukus = Buku.objects.get(id=1)

#         # pk = kwargs.get('pk')
#         # pinjam = get_object_or_404(Buku, pk=pk)
#         # bukus = Buku.objects.get(id=)
#         context = super(AddPinjamView, self).get_context_data(*args, **kwargs)
#         context["id"] = 1
#         return context 
def AddPinjamView(request, *args, **kwargs):
    pk = kwargs.get('pk')
    bukus = Buku.objects.get(id=pk)
    return render(request, 'pinjam/pinjam_add.html',{'bukus':bukus})


def CreatePinjamView(request, *args, **kwargs):
    pk = kwargs.get('pk')
    bukus = Buku.objects.get(id=pk)
    juduls = str(bukus.judul_buku)
    current_request = CrequestMiddleware.get_request()
    user = current_request.user.id

    userss = User.objects.get(id=user)
    obj = PinjamBuku(judul_buku=f"{juduls}",kd_buku=bukus, peminjam_nama=userss)
    obj.save()
    # return HttpResponse(str(obj))
    return HttpResponseRedirect('/pinjam/rak/')

    # if request.method == 'POST':
    #     obj = PinjamBuku(judul_buku=f"{juduls}",kd_buku=bukus, peminjam_nama=userss)
    #     obj.save()
    #     return HttpResponse(str(obj))
    # return render(request, 'pinjam/rak.html',{})
    # return HttpResponseRedirect('/presensi/data-kehadiran/')

      
        
# class AddPinjamView(CreateView):
#     model = PinjamBuku
#     form_class = AddBukuForm
#     template_name = 'pinjam/pinjam_add.html'
#     success_url = reverse_lazy('home')
    
#     def get_context_data(self, *args, **kwargs):
#         path = str(self.request.get_full_path())
#         id_buku = int(re.search(r'\d+', path).group())
#         bukus = Buku.objects.get(id=id_buku)
#         juduls = str(bukus.judul_buku)
        
#         current_request = CrequestMiddleware.get_request()
#         user = current_request.user.id
#         userr_id = str(current_request.user.username)
#         userss = User.objects.get(id=user)
#         # usern = str(userss.id)
        
#         if self.request.method == 'POST':
#             #     obj = PinjamBuku.objects.create(kd_buku=bukus)
#             obj = PinjamBuku(judul_buku=f"{juduls}",kd_buku=bukus, peminjam_nama=userss)
#             obj.save()

#         # buku = Buku.objects.get(kd_buku='') 
#         context = super(AddPinjamView, self).get_context_data(*args, **kwargs)
#         context["urlss"] = bukus
               
#         return context  

    
    
   
class RakView(ListView):
    model = PinjamBuku
    template_name = 'pinjam/rak.html'
    ordering = ['tanggal_pinjam']
    def get_context_data(self, *args, **kwargs):
        current_request = CrequestMiddleware.get_request()
        user = current_request.user.id
        userss = User.objects.get(id=user)
        
        now1 = datetime.datetime.now().date()
        context = super(RakView, self).get_context_data(*args, **kwargs)
        context['pinjam'] = PinjamBuku.objects.filter(tanggal_berakhir__gte=f'{now1}', peminjam_nama=userss )
        return context
    
class RiwayatView(ListView):
    model = PinjamBuku
    template_name = 'pinjam/riwayat.html'
    ordering = ['tanggal_pinjam']
    def get_context_data(self, *args, **kwargs):
        current_request = CrequestMiddleware.get_request()
        user = current_request.user.id
        userss = User.objects.get(id=user)
        
        now1 = datetime.datetime.now().date()
        context = super(RiwayatView, self).get_context_data(*args, **kwargs)
        context['pinjam'] = PinjamBuku.objects.filter(tanggal_berakhir__lte=f'{now1}', peminjam_nama=userss )
        return context
    
    
# def Rak_Render_pdf(request, *args, **kwargs):
#     pk = kwargs.get('pk')
#     pinjam = get_object_or_404(PinjamBuku, pk=pk)
#     patth = 'file1.pdf'
#     return HttpResponse(patth)
    