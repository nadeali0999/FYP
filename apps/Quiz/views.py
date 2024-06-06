from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Quiz, Question

def quiz_start(request, course_slug, quiz_id):
    return render(request, 'Quiz/quiz_startpage.html')
def quiz_detail(request, course_slug, quiz_id):
    course = get_object_or_404(Course, slug=course_slug)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        correct_answers = {str(question.id): question.correct_answer for question in questions}

        # Collect user responses and calculate the score
        user_answers = {key: request.POST.get(key) for key in correct_answers.keys()}
        for question_id, correct_answer in correct_answers.items():
            if user_answers.get(question_id) == correct_answer:
                score += 1

        # Calculate additional result data
        percent = (score / total_questions) * 100 if total_questions > 0 else 0
        return render(request, 'Quiz/quiz_result.html', {
            'course': course,
            'quiz': quiz,
            'score': score,
            'percent': percent,
            'correct': score,
            'wrong': total_questions - score,
            'total': total_questions
        })

    return render(request, 'Quiz/quiz_detail.html', {'course': course, 'quiz': quiz, 'questions': questions})