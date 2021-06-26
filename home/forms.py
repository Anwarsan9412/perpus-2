from django import forms
from .models import PinjamBuku



class AddBukuForm(forms.ModelForm):
    class Meta:
        model = PinjamBuku
        fields = ('kd_buku','judul_buku', 'peminjam_nama')

        widgets = {
            'judul_buku': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'judul','type':'hidden'}),
            # 'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Title', 'value': '', 'id':'aut','type':'hidden' }),
            # 'author': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'anwar', 'type':'hidden'}),
            'kd_buku': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'kd_bukus', 'type':'hidden'}),
            'peminjam_nama': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'anwar', 'type':'hidden'}),
            # 'category': forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            # 'body': forms.Textarea(attrs={'class':'form-control'}),
            # 'tanggal_berakhir': forms.DateField(attrs={'class':'form-control'}),
            # 'publish': forms.DateTimeField(attrs={'class':'form-control'}),
            
        }