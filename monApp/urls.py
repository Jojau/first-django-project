from django.urls import path
from . import views

app_name='monApp'
urlpatterns = [
    path('', views.index, name="index"),
    path('question/create', views.createQuestion, name="createQuestion"),
    path('question/store', views.storeQuestion, name="storeQuestion"),
    path('question/edit/<int:idQuestion>', views.editQuestion, name="editQuestion"),
    path('question/update', views.updateQuestion, name="updateQuestion"),
    path('question/delete/<int:idQuestion>', views.deleteQuestion, name="deleteQuestion"),
]