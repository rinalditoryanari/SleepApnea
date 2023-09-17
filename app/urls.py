from django.urls import path
from django.shortcuts import redirect
from .view import landing
from .view import eeg, ecg

urlpatterns = [
    path('', lambda request: redirect('landing-page')),

    path("landing-page", landing.landingpage, name="landing-page"),

    # Model
    path('api/predict-eeg', eeg.predict_api, name='api_predicteeg'),
    path('api/predict-ecg', ecg.predict_api, name='api_predictecg'),

]
