from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from publisher.models import Publisher
from django.forms import ModelForm


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['id', 'Author', 'Book', 'address', 'city', 'state_province', 'country']


def publisher_list(request, template_name='publisher/publisher_list.html'):
    posts = Publisher.objects.all()
    data = dict()
    data['object_list'] = posts
    return render(request, template_name, data)


def create_publisher(request, template_name='publisher/Publisher_form.html'):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publisher:publisher_list')
    return render(request, template_name, {'form': form})


def update_publisher(request, pk, template_name='publisher/Publisher_form.html'):
    post = get_object_or_404(Publisher, pk=pk)
    form = PublisherForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('publisher:publisher_list')
    return render(request, template_name, {'form': form})


def delete_publisher(request, pk, template_name='publisher/delete_publisher.html'):
    post = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('publisher:publisher_list')
    return render(request, template_name, {'object': post})
