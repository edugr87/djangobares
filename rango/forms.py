from django import forms
from rango.models import Bares, Tapas

class BaresForm(forms.ModelForm):
    nombre=forms.CharField(max_length=128, help_text="Introduzca nombre del bar: ")
    direccion=forms.CharField(max_length=128, help_text="Introduzca la direccion: ")
    visitas = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        
        model = Bares
        fields=('nombre','direccion','visitas')
        
class TapasForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduzca el nombre de la tapa: ")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('nombrebar',)
        #or specify the fields to include (i.e. not include the category field)
        fields = ('nombre', 'votos')