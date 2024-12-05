from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


# Create your views here.
class Registration(CreateView):
        form_class = CustomUserCreationForm
        template_name = 'blog/register.html'
        # redirect the user to login url after succesful login
        success_url = reverse_lazy('login')

@login_required
def profile(request):
        if request.method == 'POST':
                form = UserChangeForm(request.POST, intance=request.user)
                if form.is_valid():
                        form.save()
                        return redirect('profile')
        else:
                form = UserChangeForm(instance=request.user)
        return render(request, 'blog/profile.html', {'form': form})



