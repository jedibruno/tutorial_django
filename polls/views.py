from django.shortcuts import render

from polls.models import Question

# Create your views here.


def list_view(request):
    questions = Question.objects.all()
    context = dict(questions=questions)
    return render(request,"polls/list.html",context)
