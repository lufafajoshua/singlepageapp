from django.shortcuts import render, get_object_or_404

import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('Agg')

import io
import base64

from .models import Mydata
from django.views import View
from django.http import JsonResponse
from .forms import DataForm
from django.template.loader import render_to_string
from django.db.models import Q




def display_data(request):
    data  = Mydata.objects.all()
    form = DataForm()

    #Code to handle API to display prices of Bitcoin in frontend
    symbol = 'XRP/USD'
    interval = '1day'
    days = 10
    api_url = f'https://api.twelvedata.com/time_series?symbol={symbol}&exchange=Binance&interval={interval}&outputsize={days}&apikey=1fe66a2f0b934211bc6f6e29fee47220'
    raw = requests.get(api_url).json()
   
    keys = raw['meta']
    print(keys)
    crypto_data = raw['values']
    print(crypto_data)
    df = pd.DataFrame.from_records(crypto_data)
    
    #Convert the datatypes to integer and Datetime
    df.datetime=pd.to_datetime(df.datetime)
    df.open=pd.to_numeric(df.open)
    df.high=pd.to_numeric(df.high)
    df.low=pd.to_numeric(df.low)
    df.close=pd.to_numeric(df.close)
    print(df)
    
    plt.figure()

    x = df['datetime']
    y1 = df['high']
    y2 = df['low']

    #Configure the chart size
    
    size = plt.figure()
    size.set_figwidth(12)
    size.set_figheight(5)

    plt.xlabel('Date')
    plt.ylabel('Prices(USD)')
    plt.title('Bit Coin Prices in USD(High/Low)')
    plt.plot(x,y1)
    plt.plot(x,y2)
    #plt.show()
   
    #Translate the plot into a png image for display in the template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_file = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_file)
    graphic = graphic.decode('utf-8')


    context = {
            'all_data':data,
            'form': form,
            'crypto_data': crypto_data,
            'graphic': graphic,
            
    } 
    return render(request, 'myapp/data.html', context)           


def save_data_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            all_data = Mydata.objects.all()
            data['html_data_list'] = render_to_string('myapp/data.html', {
                'all_data': all_data
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)  
       
    


def update(request, pk):
    data_object = get_object_or_404(Mydata, pk=pk)
    print(pk)
    print(data_object)
    if request.method == 'POST':
        form = DataForm(request.POST, instance=data_object)
    else:
        form = DataForm(instance=data_object)

    return save_data_form(request, form, 'myapp/includes/update.html')
    
   
def search(request):
    data = dict()
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit-btn')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(address__icontains=query) | Q(telephone__icontains=query) | Q(marital_status__icontains=query) | Q(gender__icontains=query) | Q(email__icontains=query)
            results= Mydata.objects.filter(lookups).distinct()    
            context = {
                'results': results,
                'submitbutton': submitbutton,
            }
            return render(request, 'myapp/data.html', context)
            
        else:
           print("Empty input") 
    else:
        print("Invalid Request")  

