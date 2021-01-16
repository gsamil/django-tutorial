from django.shortcuts import render
from django.views import View  # BASE VIEW CLASS


class CourseView(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
