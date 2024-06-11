from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import QuizForm
from .models import Course, Quiz, Question, QuizAttempt, UserAnswer


def quiz_start(request, course_slug, quiz_id):
    course = get_object_or_404(Course, slug=course_slug)
    quiz = get_object_or_404(Quiz, id=quiz_id, course=course)

    context = {
        'course': course,
        'quiz': quiz,
    }
    return render(request, 'Quiz/quiz_startpage.html', context)


# def quiz_detail(request, course_slug, quiz_id):
#     course = get_object_or_404(Course, slug=course_slug)
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     questions = quiz.questions.all()
#
#     if request.method == 'POST':
#         score = 0
#         total_questions = questions.count()
#         correct_answers = {str(question.id): question.correct_answer for question in questions}
#
#         # Collect user responses and calculate the score
#         user_answers = {key: request.POST.get(key) for key in correct_answers.keys()}
#         for question_id, correct_answer in correct_answers.items():
#             if user_answers.get(question_id) == correct_answer:
#                 score += 1
#
#         # Calculate additional result data
#         percent = (score / total_questions) * 100 if total_questions > 0 else 0
#         return render(request, 'Quiz/quiz_result.html',
#                       {'course': course, 'quiz': quiz, 'score': score, 'percent': percent, 'correct': score,
#                        'wrong': total_questions - score, 'total': total_questions})
#
#     return render(request, 'Quiz/quiz_detail.html', {'course': course, 'quiz': quiz, 'questions': questions})


def quiz_detail(request, course_slug, quiz_id):
    course = get_object_or_404(Course, slug=course_slug)
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        form = QuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            quiz_attempt = QuizAttempt.objects.create(user=request.user, quiz=quiz)
            score = 0
            for question in quiz.questions.all():
                selected_option = form.cleaned_data.get(f'question_{question.id}')
                UserAnswer.objects.create(
                    quiz_attempt=quiz_attempt,
                    question=question,
                    selected_option=selected_option
                )
                if selected_option == question.correct_answer:
                    score += 1
            quiz_attempt.score = score
            quiz_attempt.save()
            return render(request, 'Quiz/quiz_result.html', {'quiz_attempt': quiz_attempt})
    else:
        form = QuizForm(quiz=quiz)

    return render(request, 'Quiz/quiz_detail.html', {'quiz': quiz, 'form': form})


@login_required
def quiz_result(request, quiz_attempt_id):
    quiz_attempt = get_object_or_404(QuizAttempt, id=quiz_attempt_id)
    return render(request, 'quiz_result.html', {'quiz_attempt': quiz_attempt})
