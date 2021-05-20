from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
import datetime

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)

def home(request):
    home_pagina = open("index.html", "rt")
    home = home_pagina.read()
    return HttpResponse(home)

def discription(request):
    discription_pagina = open("discription.html", "rt")
    discription = discription_pagina.read()
    return HttpResponse(discription)

def program(request):
    program_pagina = open("program.html", "rt")
    program = program_pagina.read()
    return HttpResponse(program)

def calculation(request):
    calculation_pagina = open("calculations.html", "rt")
    calculation = calculation_pagina.read()
    return HttpResponse(calculation)

urlpatterns = [
    path("", home),
    path("discription", discription),
    path("program", program),
    path("calculation", calculation),
]

execute_from_command_line()
