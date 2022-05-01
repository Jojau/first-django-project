from audioop import reverse
from django.shortcuts import redirect, render

from monApp.models import Question

# Create your views here.
def index(request):
    questions=Question.objects.all()
    context={"questions": questions}
    return render(request, 'monApp/index.html', context)

# Modèle : Question
def createQuestion(request):
    return render(request, 'monApp/models/question/create.html')

def storeQuestion(request):
    a=Question(text=request.POST["text"])
    a.save()
    return redirect('monApp:index')

def editQuestion(request, idQuestion):
    context={"question": Question.objects.get(id=idQuestion)}
    return render(request, 'monApp/models/question/edit.html', context)

def updateQuestion(request):
    question=Question.objects.get(id=request.POST["id"])
    question.text=request.POST["text"]
    question.save()
    return redirect('monApp:index')

def deleteQuestion(request, idQuestion):
    question=Question.objects.get(id=idQuestion)
    question.delete()
    return redirect('monApp:index')