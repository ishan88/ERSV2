<<<<<<< HEAD
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
import datetime

def home(request):
    return render(request,'api/index.html',{ 'clock': datetime.datetime.now() }
)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 680f91b712db3ce989e815f8ecdf12c5541a001a
