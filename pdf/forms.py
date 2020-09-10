from django import forms
from .models import Image,IncomeStatement,PositionStatemement,CashflowStatemement,AddField


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title','file')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
        }
       
class  IncomeStatementForm(forms.ModelForm):

    class Meta:
        model = IncomeStatement
        fields = ('revenue1','revenue2','tax1','tax2','profit1','profit2','year1','year2','operations1','operations2','profitTax1','profitTax2','earnings1','earnings2','expenses1','expenses2','add_name1',
        'add_name2','add_value1','add_value2','add_value3','add_value4')   

class  PositionStatementForm(forms.ModelForm):
    
    class Meta:
        model = PositionStatemement
        fields = ('totalFixed1','totalFixed2','totalCurrent1','totalCurrent2','totalAssets1','totalAssets2','equity1','equity2','totalLiab1','totalLiab2','total1','total2','year1','year2','addB_name1',
        'addB_name2','addB_value1','addB_value2','addB_value3','addB_value4')   
         

class  CashflowStatementForm(forms.ModelForm):
    
    class Meta:
        model = CashflowStatemement
        fields = ('cashOperations1','cashOperations2','cashInvesting1','cashInvesting2','cashFinancing1','cashFinancing2','netBalance1','netBalance2','year1','year2','addC_name1',
        'addC_name2','addC_value1','addC_value2','addC_value3','addC_value4')   
          


class  AddFieldForm(forms.ModelForm):
    
    class Meta:
        model = AddField
        fields = ('name','value1','value2')          
