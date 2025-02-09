from django.forms import ModelForm 
from .models import Mahasiswa


class MahasiswaForm (ModelForm):
    class Meta:
        model = Mahasiswa
        fields = "__all__"