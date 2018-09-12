from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from .models import Comentario
from .forms import CommentForm

# Create your views here.
def index(request):
    latest_comments_list = Comentario.objects.order_by('-pub_date')
    #template = loader.get_template('tarea1/index.html')
    context ={
        'latest_comments_list': latest_comments_list,
    }
    # output = ', '.join([q.mensaje for q in latest_comments_list])
    #return HttpResponse(template.render(context, request))
    return render(request, 'tarea1/index.html', context)

def new_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            new_comment = Comentario(mensaje=form.cleaned_data['new_comment'],
                                     pub_date=timezone.now(),
                                     IP_cliente=ip)
            new_comment.save()
            return HttpResponseRedirect('/tarea1')
    else:
        form = CommentForm()

    return render(request, 'index.html', {'form': form})
