from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import InstaRegistrationForm, UserUpdateForm, ProfileUpdateFoem
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = InstaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = InstaRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateFoem()

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)


