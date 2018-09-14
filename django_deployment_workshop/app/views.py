from django.shortcuts import render

from django.http import HttpResponse
import datetime

from django.views import View


class Time(View):

    def get(self, request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)
