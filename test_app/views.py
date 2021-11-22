from django.shortcuts import render

from .models import Posts
from .forms import ChoiceNameForm


def get_name(request):
    if request.method == 'POST':
        form = ChoiceNameForm(request.POST)
        if form.is_valid():
            if 'all' in request.POST:
                form = ChoiceNameForm()
                queryset = Posts.objects.select_related('userId').all()

                return render(request, 'test_app/index.html', {'form': form, 'posts': queryset})
            ch = form.cleaned_data.get('choice')
            queryset = Posts.objects.select_related('userId').all().filter(userId=ch)

            return render(request, 'test_app/index.html', {'form': form, 'posts': queryset})
    else:
        form = ChoiceNameForm()
        queryset = Posts.objects.select_related('userId').all()
        return render(request, 'test_app/index.html', {'form': form, 'posts': queryset})
