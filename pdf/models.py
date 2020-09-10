from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='docs',default='null')
    

    def __str__(self):
        return self.title
#year,revenue,operations,profitTax,tax,profit 
class IncomeStatement(models.Model):
    year1 = models.CharField(max_length=100, null=True)
    year2 = models.CharField(max_length=100, null=True)
    revenue1 = models.CharField(max_length=100, null=True)
    revenue2 = models.CharField(max_length=100, null=True)
    operations1 = models.CharField(max_length=100, null=True)
    operations2 = models.CharField(max_length=100, null=True)
    profitTax1 = models.CharField(max_length=100, null=True)
    profitTax2 = models.CharField(max_length=100, null=True)
    tax1 = models.CharField(max_length=100, null=True)
    tax2 = models.CharField(max_length=100, null=True)
    profit1 = models.CharField(max_length=100, null=True)
    profit2 = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    earnings1 = models.CharField(max_length=20, null=True)
    earnings2 = models.CharField(max_length=20, null=True)
    expenses1 = models.CharField(max_length=20, null=True)
    expenses2 = models.CharField(max_length=20, null=True)
    add_name1 = models.CharField(max_length=20, null=True,blank=True)
    add_name2 = models.CharField(max_length=20, null=True,blank=True)
    add_value1 = models.CharField(max_length=20, null=True,blank=True)
    add_value2 = models.CharField(max_length=20, null=True,blank=True)
    add_value3 = models.CharField(max_length=20, null=True,blank=True)
    add_value4 = models.CharField(max_length=20, null=True,blank=True)

    def __str__(self):
        return self.year1

class PositionStatemement(models.Model):
    year1 = models.CharField(max_length=20, null=True)
    year2 = models.CharField(max_length=20, null=True)
    totalFixed1 = models.CharField(max_length=20, null=True)
    totalFixed2 = models.CharField(max_length=20, null=True)
    totalCurrent1 = models.CharField(max_length=20, null=True)
    totalCurrent2 = models.CharField(max_length=20, null=True)
    totalAssets1 = models.CharField(max_length=20, null=True)
    totalAssets2 = models.CharField(max_length=20, null=True)
    equity1 = models.CharField(max_length=20, null=True)
    equity2 = models.CharField(max_length=20, null=True)
    totalLiab1 = models.CharField(max_length=20, null=True)
    totalLiab2 = models.CharField(max_length=20, null=True)
    total1 = models.CharField(max_length=20, null=True)
    total2 = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    addB_name1 = models.CharField(max_length=20, null=True,blank=True)
    addB_name2 = models.CharField(max_length=20, null=True,blank=True)
    addB_value1 = models.CharField(max_length=20, null=True,blank=True)
    addB_value2 = models.CharField(max_length=20, null=True,blank=True)
    addB_value3 = models.CharField(max_length=20, null=True,blank=True)
    addB_value4 = models.CharField(max_length=20, null=True,blank=True)
    


    def __str__(self):
        return self.year1        

class CashflowStatemement(models.Model):
    year1 = models.CharField(max_length=20, null=True)
    year2 = models.CharField(max_length=20, null=True)
    cashOperations1 = models.CharField(max_length=20, null=True)
    cashOperations2 = models.CharField(max_length=20, null=True)
    cashInvesting1 = models.CharField(max_length=20, null=True)
    cashInvesting2 = models.CharField(max_length=20, null=True)
    cashFinancing1 = models.CharField(max_length=20, null=True)
    cashFinancing2 = models.CharField(max_length=20, null=True)
    netBalance1 = models.CharField(max_length=20, null=True)
    netBalance2 = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    addC_name1 = models.CharField(max_length=20, null=True,blank=True)
    addC_name2 = models.CharField(max_length=20, null=True,blank=True)
    addC_value1 = models.CharField(max_length=20, null=True,blank=True)
    addC_value2 = models.CharField(max_length=20, null=True,blank=True)
    addC_value3 = models.CharField(max_length=20, null=True,blank=True)
    addC_value4 = models.CharField(max_length=20, null=True,blank=True)

    def __str__(self):
        return self.year1        

class  AddField(models.Model):
    name = models.CharField(max_length=20, null=True)
    value1 = models.CharField(max_length=200, null=True)
    value2 = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name 


