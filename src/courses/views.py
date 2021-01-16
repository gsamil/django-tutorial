from django.shortcuts import render, get_object_or_404
from django.views import View  # BASE VIEW CLASS
from .models import Course


class CourseView(View):
    template_name = "courses/course_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
