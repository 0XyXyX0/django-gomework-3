from django.shortcuts import render
import random
import names


students = []
def get_random_students(num_students=100):

    for _ in range(num_students):
        student = {
            'name': names.get_first_name(),
            'surname': names.get_last_name(),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
        
    return students

get_random_students()



def main_page_view(request):
    context = {
        'name': names.get_first_name(),
        'surname': names.get_last_name(),
        'gpa': round(random.uniform(1.0, 4.0), 2),
        'course': random.randint(1, 4)
    }
    return render(request, "main_page.html", context=context)


def students_page_view(request):
    context = {
        "list": students
    }
    return render(request, "students_page.html", context=context)