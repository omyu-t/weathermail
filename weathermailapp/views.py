from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()

from .forms import UserCreateForm, LoginForm



# Create your views here.


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('register_comp')




def registercomp(request):
    return render(request, 'register_comp.html', {'message': '登録が完了しました'})


def delete(request, pk):
    user_info = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user_info.delete()
        return redirect('delete_comp')

    return render(request, 'delete.html', {'User': user_info})


def deletecomp(request):
    return render(request, 'delete_comp.html', {'message': '削除しました'})


@login_required
def update(request, pk):
    user = get_object_or_404(User, pk=pk)

    pk = request.user.id

    form = UserCreateForm(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('register_comp')

    context = {
        'form': form,
        'pk': pk
    }
    return render(request, 'update.html', context)



def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        obj = User.objects.get(username=username)
        pk = obj.id
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('update', pk=pk)
        else:
            return render(request, 'login.html', {
                'error': 'ユーザーネームかパスワードが違います', 
                'form': LoginForm
            })

    return render(request, 'login.html', {'form': LoginForm})


def logoutfunc(request):
    logout(request)
