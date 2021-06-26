from django.http import request
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Buku

class HomeView(ListView):
    model = Buku
    template_name= 'home.html'
    ordering =['-published']
    fields = '__all__'
        
    def get_context_data(self, *args, **kwargs):
        buku = Buku.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['heading'] = "Halaman Home"
        context['buku'] = buku
        return context
    
def CategoryView(request, *args, **kwargs):
    pk = kwargs.get('pk')
    # print(pk)
    bukus = Buku.objects.filter(buku_category=pk)
    cat = Buku.objects.filter(buku_category=pk).values("buku_category").distinct()
    print(bukus)
    return render(request, 'category.html',{'buku':bukus, 'cat':cat})
        
def Search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        buku = Buku.objects.filter(judul_buku__contains=searched)
        return render(request, 'search.html',{'buku':buku,'searched':searched})
    else:               
        return render(request, 'home.html',{})


    
