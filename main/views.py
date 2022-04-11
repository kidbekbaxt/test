from django.shortcuts import render
from .models import Question, Answer


def main_index(request):
    show_answer = False
    total = 0
    right = 0
    if request.method == 'POST':
        question_id = [int(k[1:]) for k in request.POST.keys() if k.startswith('q')]
        answer_id = {}
        for qid in question_id:
            answer_id[qid] = int(request.POST.get(f"q{qid}"))

        questions = Question.objects.filter(id__in=question_id).all()

        for q in questions:
            total += q.ball

        for a in q.answer_set.all():
            # ushbu ifoda faqat bitta javob to'g'ri bo'lgani uchun ishlaydi
            # Umuman testimiz faqat bitta 1 ta javob to'g'ri holatlar uchun ishlaydi

            if answer_id[q.id] == a.id and a.is_right:
                right += q.ball

        show_answer = True

    return render(request, 'main/index.html', {
        'show_answer': show_answer,
        'total': total,
        'right': right,
        # tasodifiy 10ta son olish
        'questions': Question.objects.order_by('?')[:10]
    })
