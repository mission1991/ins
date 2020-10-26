from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    #회원가입 완료상태
    if request.method == 'POST':
        user_from = RegisterForm(request.POST)
        if user_from.is_valid():
            new_user = user_from.save(commit=False)
            new_user.set_password(user_from.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        #회원가입 진행상태
        user_form = RegisterForm()
        return render(request, 'registration/register.html', {'form':user_form})