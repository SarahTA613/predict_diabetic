from django.shortcuts import render
from django.views import View
import pickle
import numpy as np
from pickle import load

model=pickle.load(open("./savedModels/model.pkl",'rb'))

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,"index.html")

    def post(self,request):
        Pregnancies=request.POST['Pregnancies']
        Glucose=request.POST['Glucose']
        BloodPressure=request.POST['BloodPressure']
        SkinThickness=request.POST['SkinThickness']
        Insulin=request.POST['Insulin']
        BMI=request.POST['BMI']
        DiabetesPedigreeFunction=request.POST['DiabetesPedigreeFunction']
        Age=request.POST['Age']
        
        diab_prediction=model.predict([[float(Pregnancies),
        float(Glucose),
        float(BloodPressure),
        float(SkinThickness),
        float(Insulin),
        float(BMI),
        float(DiabetesPedigreeFunction),
        float(Age)
        ]])
        if diab_prediction[0]==0:
            diab_diagnosis = 'Patient is not Diabetic'
        else:
            diab_diagnosis = 'Patient is Diabetic'
        
    
           
        return render(request,"index.html",{'result':diab_diagnosis})

