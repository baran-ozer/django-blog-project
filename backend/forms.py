from django import forms

class PackageForm(forms.Form):
    en = forms.IntegerField(label='En', max_value=999, min_value=1)
    boy = forms.IntegerField(label='Boy', max_value=999, min_value=1)
    yukseklik = forms.IntegerField(label='Yükseklik', max_value=999, min_value=1)
    agirlik = forms.IntegerField(label='Ağırlık', max_value=999, min_value=1)

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'