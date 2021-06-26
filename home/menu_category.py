from .models import BukuCategory


def category_menu(request):
    cat_buku = BukuCategory.objects.all()
    return {
         'cat_menu': cat_buku
    }  