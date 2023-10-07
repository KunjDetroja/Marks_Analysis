from django import forms
from .models import Marksheet


class Marks(forms.ModelForm):
    class Meta:
        model = Marksheet
        fields = ['DM_T1', 'DM_T2', 'DM_T3', 'DM_T4', 'FSD_2_T1', 'FSD_2_T2', 'FSD_2_T3', 'FSD_2_T4', 'TOC_T1', 'TOC_T2',
                  'TOC_T3', 'TOC_T4', 'FCSP_2_T1', 'FCSP_2_T2', 'FCSP_2_T3', 'FCSP_2_T4', 'COA_T1', 'COA_T2', 'COA_T3', 'COA_T4']
