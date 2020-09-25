from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
from django.core import serializers
from .models import IncomeStatement,PositionStatemement,CashflowStatemement
from django.utils import timezone
from .forms import IncomeStatementForm,PositionStatementForm,CashflowStatementForm,ImageForm,AddFieldForm
import tabula
import numpy as np
import pandas as pd
import re
import os
# Read pdf into list of DataFrame




#Convert pdf to image
import tempfile

from pdf2image import convert_from_path
# Create your views here.

def convertDF(excel):
    customers = pd.read_excel(excel)
    return customers


def Exract(pdf_file):
    df = tabula.read_pdf(pdf_file, pages='3')
    return df[1]


def ExtractBalance(pdf_file):
    df = tabula.read_pdf(pdf_file, pages='3')
    return df[3]

def ExtractCash(pdf_file):
    df = tabula.read_pdf(pdf_file, pages='3')
    return df[5]

def Clean(df):
    df = pd.DataFrame(df)
    return df.dropna(thresh=5,axis=1)    

def SearchIncome(df):
    #df = Extract(pdf_file)
    revenue,operations,profitTax,tax,profit = 0,0,0,0,0
    
    year = df.columns.tolist()
    for row_index,row in df.iterrows():

        rev = re.search("TOTAL.REV", str(row[0]))
        if(rev):
            revenue = [row[1],row[2]]
            print(revenue) 

        op = re.search("from.operat", str(row[0]))
        if(op):
            operations = [row[1],row[2]]
            print(operations) 

        pt = re.search("before.tax", str(row[0]))
        if(pt):
            profitTax = [row[1],row[2]]
            print(profitTax)    

        tax1 = re.search("Income tax", str(row[0]))
        if(tax1):
            tax = [row[1],row[2]]
            print("Tax is:")
            print(tax)
            
        profit1 = re.search("from.operations", str(row[0]))
        if(profit1):
            profit = [row[1],row[2]]
            print(profit)
    return year,revenue,operations,profitTax,tax,profit        

def SearchBalance(df):
    #df = Extract(pdf_file)
    totalFixed,totalCurrent,totalAssets,totalEquity,totalLiab,totals = 0,0,0,0,0,0
    
    year = df.columns.tolist()
    for row_index,row in df.iterrows():

        fix = re.search("otal.fixed", str(row[0]))
        if(fix):
            totalFixed = [row[1],row[2]]
            print(totalFixed) 

        totalFixed = ['0','0']
        cur = re.search("otal.curr", str(row[0]))
        if(cur):
            totalCurrent = [row[1],row[2]]
            print(totalCurrent) 
        totalCurrent = ['0','0']

        ass = re.search("otal.assets", str(row[0]))
        if(ass):
            totalAssets = [row[1],row[2]]
            print(totalAssets)    

        equ = re.search("otal.equity$", str(row[0]))
        if(equ):
            totalEquity = [row[1],row[2]]
            
        liab = re.search("otal.liabilities", str(row[0]))
        if(liab):
            totalLiab = [row[1],row[2]]
            print(totalLiab)
            
        total = re.search("otal.equity.and", str(row[0]))
        if(total):
            totals = [row[1],row[2]]
            print(totals)    
    return totals,totalLiab,totalEquity,totalAssets,totalCurrent,totalFixed        

def SearchCash(df):
    #df = Extract(pdf_file) investing activities from.operating /.from.financing.activities
    operations,investing,financing,netTotal = 0,0,0,0
    
    year = df.columns.tolist()
    for row_index,row in df.iterrows():

        fix = re.search("operating.activities", str(row[0]))
        if(fix):
            operations = [row[1],row[2]]
            print(operations) 


        cur = re.search("investing.activities", str(row[0]))
        if(cur):
            investing = [row[1],row[2]]
            print(investing) 
        

        ass = re.search("financing.activities", str(row[0]))
        if(ass):
            financing = [row[1],row[2]]
            print(financing)    

        fix = re.search("equivalents.at.end", str(row[0]))
        check = True
        if(fix and check):
            check =False
            netTotal = [row[1],row[2]]
            print(netTotal)   
    return netTotal,financing,investing,operations        

def convertImage(pdf_file):
    pages = convert_from_path(pdf_file, 300)
    pdf_file = pdf_file[:-4]
    imagesList = []

    for page in pages:
        page.save("%s-page%d.jpg" % (pdf_file,pages.index(page)), "JPEG")
        ngoni = "%s-page%d.jpg" % (pdf_file,pages.index(page))
        #imagesList[pages.index(page)] = ngoni
        print("now printing:%s"%(ngoni))
        imagesList.append(ngoni[19:])
       # imagesList.append("%s-page%d.jpg" % (pdf_file,pages.index(page)))
    print("finished")  
    print("Dictionary is : ",imagesList) 
    return imagesList



def display(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            print("now printing obj Image")
            print(str(img_obj.file.url))

            print("------------------------")
            print("now converting pdf")
            ngoni = convertImage(img_obj.file.path)
            print("2nd Dictionary is : ",ngoni)
            ngodza = Exract(img_obj.file.path)
            #images_from_path = convert_from_path("E:/ngoni/edgars.pdf", fmt="jpeg")
            return render(request, 'form.html', {'form':form,'ngoni': ngoni, 'ngodza': ngodza})
        print('form invalid')    
    form = ImageForm()
    
    return render(request, 'form.html', {'form': form})

def view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            print("now printing obj Image")
            print(str(img_obj.file.url))
            filename, file_extension = os.path.splitext(img_obj.file.path)
            if(file_extension=='.xls'):
                drop = convertDF(img_obj.file.path)
                pos = drop
                cash = drop
                ngoni =[]
                ngodza = []

            else:
                ngoni = convertImage(img_obj.file.path)
                ngodza = Exract(img_obj.file.path)
                muna = ExtractBalance(img_obj.file.path)
                nyasha =ExtractCash(img_obj.file.path)
                drop = Clean(ngodza)
                pos = Clean(muna)
                cash = Clean(nyasha)



            print("------------------------")
            print("now converting pdf")

            




            print("-------------- Finished Extracting ---------------------------------")

            

            print("-------------- Finished cleaning ---------------------------------")
            look = SearchIncome(drop)
            sheet = SearchBalance(pos)
            lid = SearchCash(cash)

            print(look)
            print(sheet)
            print("-------------- Finished searching ---------------------------------")
            #print("2nd Dictionary is : ",ngoni)
            #ngodza = Exract(img_obj.file.path)
            
            print("-------------------Now Printing Year---------------------------")
            year = look[0]
            revenue = look[1]
            operations = look[2]
            profitTax = look[3]
            tax = look[4]
            profit = look[5]
            print("------------------------Now getting Balance Sheet Iterms-----------------")

            totals = sheet[0]
            totalLiab = sheet[1]
            totalEquity = sheet[2]
            totalAssets = sheet[3]
            totalCurrent = sheet[4]
            totalFixed = sheet[5]
            print(totalFixed)
            
            print("------------------------Now getting Cash Flow Sheet Iterms-----------------")
            netTotal = lid[0]
            financing = lid[1]
            investing = lid[2]
            operations = lid[3] #netTotal,financing,investing,operations
 
            images_from_path = convert_from_path("E:/ngoni/edgars.pdf", fmt="jpeg")
            return render(request, 'view.html', {'form':form,'ngoni': ngoni, 'ngodza': ngodza,'year':year,
            'revenue':revenue,'operations':operations,'profitTax':profitTax,'tax':tax,'profit':profit,
            'totals':totals,'totalLiab':totalLiab,'totalEquity':totalEquity,'totalAssets':totalAssets,'totalCurrent':totalCurrent,
            'totalFixed':totalFixed,'netTotal':netTotal,'investing':investing,'financing':financing,'operations':operations})
        print('form invalid')    
    form = ImageForm()  #year,revenue,operations,profitTax,tax,profit 
    
    return render(request, 'form.html', {'form': form})

def index(request):
    form = ImageForm()
    return render(request,'form.html',{'form':form})

def save(request):
    if request.method == 'POST':
 
        form = IncomeStatementForm(request.POST)
        form2 = PositionStatementForm(request.POST)
        form3 = CashflowStatementForm(request.POST)
        print(form2)
        print(form3)
        if form.is_valid():
            print(request.POST)
            obj = IncomeStatement()
         #gets new object
            obj.year1 = form.cleaned_data['year1']
            obj.year2 = form.cleaned_data['year2']
            obj.revenue1 = form.cleaned_data['revenue1']
            obj.revenue2 = form.cleaned_data['revenue2']
            obj.expenses1 = form.cleaned_data['expenses1']
            obj.expenses2 = form.cleaned_data['expenses2']
            obj.operations1 = form.cleaned_data['operations1']
            obj.operations2 = form.cleaned_data['operations2']
            obj.profitTax1 = form.cleaned_data['profitTax1']
            obj.profitTax2 = form.cleaned_data['profitTax2']
            obj.tax1 = form.cleaned_data['tax1']
            obj.tax2 = form.cleaned_data['tax2']
            obj.profit1 = form.cleaned_data['profit1']
            obj.profit2 = form.cleaned_data['profit2']
            obj.earnings1 = form.cleaned_data['earnings1']
            obj.earnings2 = form.cleaned_data['earnings1']
            obj.add_name1 = form.cleaned_data['add_name1']
            obj.add_name2 = form.cleaned_data['add_name2']
            obj.add_value1 = form.cleaned_data['add_value1']
            obj.add_value2 = form.cleaned_data['add_value2']
            obj.add_value3 = form.cleaned_data['add_value3']
            obj.add_value4 = form.cleaned_data['add_value4']

              #gets new object
            obj.save()  

            cash = PositionStatemement()  

       
            cash.year1 = form.cleaned_data['year1']
            cash.year2 = form.cleaned_data['year2']
            cash.totalFixed1 = form2.cleaned_data['totalFixed1']
            cash.totalFixed2 = form2.cleaned_data['totalFixed2']
            cash.totalCurrent1 = form2.cleaned_data['totalCurrent1']
            cash.totalCurrent2 = form2.cleaned_data['totalCurrent2']
            cash.totalAssets1 = form2.cleaned_data['totalAssets1']
            cash.totalAssets1 = form2.cleaned_data['totalAssets2']
            cash.equity1 = form2.cleaned_data['equity1']
            cash.equity2 = form2.cleaned_data['equity2']
            cash.totalLiab1 = form2.cleaned_data['totalLiab1']
            cash.totalLiab2 = form2.cleaned_data['totalLiab2']
            cash.total1 = form2.cleaned_data['total1']
            cash.total2 = form2.cleaned_data['total2']
 #           cash.addB_name1 = form.cleaned_data['addB_name1']
 #           cash.addB_name2 = form.cleaned_data['addB_name2']
 #           cash.addB_value1 = form.cleaned_data['addB_value1']
 #           cash.addB_value2 = form.cleaned_data['addB_value2']
 #           cash.addB_value3 = form.cleaned_data['addB_value3']
 #           cash.addB_value4 = form.cleaned_data['addB_value4']

            #finally save the object in db
            cash.save()

            cash1 = CashflowStatemement()

                          #gets new object
            cash1.year1 = form.cleaned_data['year1']
            cash1.year2 = form.cleaned_data['year2']
            cash1.cashOperations1 = form3.cleaned_data['cashOperations1']
            cash1.cashOperations2 = form3.cleaned_data['cashOperations2']
            cash1.cashInvesting1 = form3.cleaned_data['cashInvesting1']
            cash1.cashInvesting2 = form3.cleaned_data['cashInvesting2']
            cash1.cashFinancing1 = form3.cleaned_data['cashFinancing1']
            cash1.cashFinancing2 = form3.cleaned_data['cashFinancing2']
            cash1.netBalance1 = form3.cleaned_data['netBalance1']
            cash1.netBalance2 = form3.cleaned_data['netBalance2']
#            cash1.addC_name1 = form3.cleaned_data['addC_name1']
#            cash1.addC_name2 = form3.cleaned_data['addC_name2']
#            cash1.addC_value1 = form3.cleaned_data['addC_value1']
#            cash1.addC_value2 = form3.cleaned_data['addC_value2']
#            cash1.addC_value3 = form3.cleaned_data['addC_value3']
#            cash1.addC_value4 = form3.cleaned_data['addC_value4']

            #finally save the object in db
            cash1.save()



            # Get the current instance object to display in the template
            income = IncomeStatement.objects.latest('created_at')
            position = PositionStatemement.objects.latest('created_at')
            cash = CashflowStatemement.objects.latest('created_at')
 
            
            return render(request, 'final.html',{'income':income,'position':position,'cash':cash} )
        print(form.errors)    
        print('form invalid')    
    
    form = ImageForm()
    return render(request, 'form.html', {'form': form})

def saveIncome(request):
    response_data = {}
    #form = IncomeStatementForm(request.POST)
    

    if request.POST.get('action') == 'post':
        year1 = request.POST.get('year1')
        year2 = request.POST.get('year2')
        revenue1 = request.POST.get('revenue1')
        revenue2 = request.POST.get('revenue2')
        operations1 = request.POST.get('operations1')
        operations2 = request.POST.get('operations2')
        profitTax1 = request.POST.get('profitTax1')
        profitTax2 = request.POST.get('profitTax2')
        tax1 = request.POST.get('tax1')
        tax2 = request.POST.get('tax2')
        profit1 = request.POST.get('profit1')
        profit2 = request.POST.get('profit2')

        response_data['year1'] = year1
        response_data['year2'] = year2
        response_data['revenue1'] = revenue1
        response_data['revenue2'] = revenue2
        response_data['operations1'] = operations1
        response_data['operations2'] = operations2
        response_data['profitTax1'] = profitTax1
        response_data['profitTax2'] = profitTax2
        response_data['tax1'] = tax1
        response_data['tax2'] = tax2
        response_data['profit1'] = profit2
        response_data['profit2'] = profit2


        IncomeStatement.objects.create(
            year1 = year1,
            year2 = year2,
            revenue1 = revenue1,
            revenue2 = revenue2,
            operations1 = operations1,
            operations2 = operations2,
            profitTax1 = profitTax1,
            profitTax2 = profitTax2,
            tax1 = tax1,
            tax2 = tax2,
            profit1 = profit1,
            profit2 = profit2,
            )
        return JsonResponse(response_data)

    return render(request, 'view.html')   

def feedback(request):
    if request.POST:
        form = AddFieldForm(request.POST)
       # form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return JsonResponse(data)
            return JsonResponse({'success':True}) 


        else:
            return JsonResponse({'error':form.errors})
    return HttpResponseRedirect('')
  
def add(request):
    return render(request, 'add.html')

def kanban(request):
    return render(request, 'drag.html')    

#              
#           