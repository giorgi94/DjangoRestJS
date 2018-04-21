from django.shortcuts import render, redirect, reverse

from .models import Person


from django.utils.translation import activate, get_language

def index(request):

    # print(get_language())

    context = {
        'names': Person.objects.all().values_list('name', flat=True)
    }

    # print('\nNames:', context.get('names'))

    return render(request, 'index.html', context)


def register(request):

    name = request.GET.get('name')

    p = Person.objects.create(name=name)

    return redirect(reverse('index'))