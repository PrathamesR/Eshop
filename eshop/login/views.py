from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.views.generic import View
from .models import Item, Order
from .forms import UserForm
from django.contrib.auth.models import User


def index(request):
    all_items = Item.objects.all()
    return render(request, 'Home.html', {'all_items': all_items})


def profile(request):
    orders = get_list_or_404(Order, user=request.user)
    #for i in orders:
        #items = Item.objects.filter(id=id)
    return render(request, 'Profile.html', {'orders': orders})


def itempage(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'ItemPage.html', context)


def typee(request, item_type):
    items = get_list_or_404(Item, itemType=item_type)
    context = {'items': items}
    return render(request, 'Type.html', context)


def confirm(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    a = Order()
    a.order = item_id
    a.item = item
    a.user = request.user
    a.save()
    return render(request, 'Confirmation.html', context)


def log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'Login.html', {'error_message': 'Invalid login'})
    return render(request, 'Login.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password, email=email)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})


def out(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Login.html', context)