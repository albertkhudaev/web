from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list_all(request):
    questions = Question.objects.all()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })