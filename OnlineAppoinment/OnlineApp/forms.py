from django import forms
from .models import *

class alumnus(forms.ModelForm):
    class Meta:
        model = AlumniBook
        fields = ['Aname','Alast','Amail','Asid','Acourse','Ayg','Adate','Adep','Apurp']

class student(forms.ModelForm):
    class Meta:
        model = StudentBook
        fields = ['Sname','Slast','Smail','Ssid','Scourse','Syear','Sdate','Sdep','Spurp']

class guardian(forms.ModelForm):
    class Meta:
        model = GuardianBook
        fields = ['Ggname','Gname','Glast','Gmail','Gsid','Gcourse','Gdate','Gdep','Gpurp']

