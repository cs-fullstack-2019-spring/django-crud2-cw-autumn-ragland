from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import ContactModel


# display all objects in model
def index(request):
    allContacts = ContactModel.objects.all()
    context = {
        'allContacts': allContacts
    }
    return render(request, 'cwApp/index.html', context)


# add contact to model using model bound form
def add(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'cwApp/add.html', context)


# update user
def edit(request, id):
    selected_contact = get_object_or_404(ContactModel, pk=id)
    edit_contact = ContactForm(request.POST or None, instance=selected_contact)
    if edit_contact.is_valid():
        edit_contact.save()
        return redirect('index')

    context = {
        'form': edit_contact,
    }
    return render(request, 'cwApp/add.html', context)


# delete user
def delete(request, id):
    selected_contact = get_object_or_404(ContactModel, pk=id)
    if request.method == 'POST':
        selected_contact.delete()
        return redirect('index')

    context = {
        'selected_contact': selected_contact,
    }
    return render(request, 'cwApp/delete.html', context)
