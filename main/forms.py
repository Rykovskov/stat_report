from .models import Report_tags, Values_tags, Trcking_tags
from django import forms

class ReportConfigForms(forms.ModelForm):
    class Meta:
        model = Trcking_tags
        fields = ['infrastructure_tag', 'service_tag', 'priority_tag', 'descr_track']
        widgets = {
            'infrastructure_tag': forms.Select(attrs={'class': 'form-input', 'style': 'width:100px'}),
            'service_tag': forms.Select(attrs={'class': 'form-input'}),
            'priority_tag': forms.Select(attrs={'class': 'form-input'}),
            'descr_track': forms.TextInput(attrs={'class': 'form-input', 'size':'10'})
        }




