from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from publisher.models import Publisher
from django.forms import ModelForm


# form for publisher model
class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['id', 'Author', 'Book', 'address', 'city', 'state_province', 'country']


# function to show publisher list
def publisher_list(request, template_name='publisher/publisher_list.html'):
    posts = Publisher.objects.all()
    data = dict()
    data['object_list'] = posts
    return render(request, template_name, data)


# function to create a publisher
def create_publisher(request, template_name='publisher/Publisher_form.html'):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publisher:publisher_list')
    return render(request, template_name, {'form': form})


# function to update a publisher
def update_publisher(request, pk, template_name='publisher/Publisher_form.html'):
    publisher = get_object_or_404(Publisher, pk=pk)
    form = PublisherForm(request.POST or None, instance=publisher)
    if form.is_valid():
        form.save()
        return redirect('publisher:publisher_list')
    return render(request, template_name, {'form': form})


# function to delete a publisher
def delete_publisher(request, pk, template_name='publisher/delete_publisher.html'):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher:publisher_list')
    return render(request, template_name, {'object': publisher})
