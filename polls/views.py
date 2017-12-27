from django.shortcuts import get_object_or_404, render
# from django.template import loader
from django.utils import timezone
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'  # 기본 컨택스트 이름은 question_list

    def get_queryset(self):
        """
        Return the last five published questions
        (not including those set to be published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question                     # 알아서 question 으로 컨택스트 제공해줌.
    template_name = 'polls/detail.html'  # 기본적으로 [app name]/[model name]_detail.html 로 설정되어 있음.
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()) # 현재 시간 보다 과거인 것만 불러오기.

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


############### Generic view 사용전 #############################################################
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#     # 아래 코드 단축버전 (HttpResponse와 loader를 import 하지 않아도 됨.)
#     context = {'latest_question_list': latest_question_list}
#     return render(request,'polls/index.html', context)
#
#     # template = loader.get_template('polls/index.html')
#     # context={
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#
#
#
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # return HttpResponse("Hello, world. You're at the polls index")
#
# def detail(request, question_id):
#     # 약결합을 위해 DoesNotExist 를 사용하지 않고 get_object_or_404를 사용.
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#     # 예외로 에러 발생 시키기
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#

###########################################################################################

    # return HttpResponse("You're voting on question %s." % question_id)
