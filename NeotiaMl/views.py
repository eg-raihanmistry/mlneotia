from django.http import HttpResponse
from django.shortcuts import render
import pickle as pkl
import sklearn
import pandas as pd
import numpy as np
import os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'randomforestregressor.pkl')
with open(model_path, 'rb') as file:
    model = pkl.load(file)

def home(request):
    predicted_price = None
    if request.method == "POST":
        carpet_area = int(request.POST['carpet_area'])
        status = request.POST['staus']
        floor = int(request.POST['floor'])
        transaction = request.POST['transaction']
        furnishing = request.POST['furnishing']
        facing = request.POST['facing']
        overlooking = request.POST['overlooking']
        bathroom = request.POST['bathroom']
        balcony = request.POST['balcony']
        car_parking = int(request.POST['car_parking'])
        ownership = request.POST['ownership']

        house_data = {
            'Carpet Area': [carpet_area], 
            'Status': [status], 
            'Floor': [floor], 
            'Transaction': [transaction], 
            'Furnishing': [furnishing], 
            'facing': [facing],
            'overlooking': [overlooking], 
            'Bathroom': [bathroom], 
            'Balcony': [balcony], 
            'Car Parking': [car_parking], 
            'Ownership': [ownership]
        }

        test_data = pd.DataFrame(house_data)
        predict = model.predict(test_data)
        predicted_price = np.expm1(predict)
        predicted_price = round(predicted_price[0], 2)

    payload = {
        'predicted_price' : predicted_price
    }

    return render(request, 'index.html', payload)

def about(request):
    return HttpResponse("About Page.")

def services(request):
    return HttpResponse("Services Page.")

def contact(request):
    return HttpResponse("Contact Page.")