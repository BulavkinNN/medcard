from django.urls import path

from . import views

app_name = 'medcard'

urlpatterns = [

    path('medcard/patient/', views.patient, name='patient'),
    path('medcard/doctor/', views.doctor, name='doctor'),
    path('medcard/', views.medcard, name='medcard'),
    # path('analysis/', views.Analysis.as_view(), name='analysis_detail'),
    path('analysis/<int:pk>', views.AnalysisDetailView.as_view(), name='analysis_detail'),
    path('disease/<int:pk>', views.DiseaseDetailView.as_view(), name='disease_detail'),
    path('', views.index, name='index'),

]