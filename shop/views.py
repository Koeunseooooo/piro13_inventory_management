from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Account



def Account_List(request):
    queryset = Account.objects.all()
    context={
        'Accounts': queryset,
    }
    return render(request, 'shop/Account_List.html', context=context)


def Account_Register(request):
    if request.method == 'GET':
        return render(request, 'shop/Account_Register.html', context={})

    Name = request.POST['Name']
    Call = request.POST['Call']
    Address = request.POST['Address']
    account = Account.objects.create(Name=Name, Call=Call, Address=Address)
    pk = account.id

    url = reverse('shop:Account_Detail', kwargs={'pk': pk})
    return redirect(to=url)


def Account_Detail(request,pk):
    account = Account.objects.get(id=pk)

    context = {
        'Account':account
    }
    return render(request, 'shop/Account_Detail.html',context=context)

def delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()

    url = reverse('shop:Account_List')
    return redirect(to=url)


def Account_Update(request, pk):
    account = Account.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'Account': account
        }
        return render(request, 'shop/Account_Update.html', context=context)

    Name = request.POST['Name']
    Call = request.POST['Call']
    Address = request.POST['Address']

    account.Name = Name
    account.Call = Call
    account.Address= Address

    account.save()

    url = reverse('shop:Account_Detail', kwargs={'pk': pk})
    return redirect(to=url)
