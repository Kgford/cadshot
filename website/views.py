from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from datetime import date
from django.urls import reverse, reverse_lazy
from django.views import View
import datetime
from django.contrib.auth.decorators import login_required
from conversions.vector_express import File_Conversions

# https://github.com/smidyo/vectorexpress-api#quickstart

class APIView(View):
    template_name = "signup.html"
    success_url = reverse_lazy('atspublic:signup')
    def get(self, *args, **kwargs):
        inv=-1
        try:
            print('in Get')
            timestamp = date.today()
            converted = File_Conversions('','','')
            url = converted .geturl_plt_svg()
            print('url=',url)
            #file = converted .getfile_plt_svg()
            #print('file=',file)
        except IOError as e:
            print('error = ',e) 
        return render(self.request,'index.html',{})