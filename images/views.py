from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            new_image = form.save(commit=False)
            # assign current user to the image
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.xhtml', {
        'section': 'images',
        'form': form
    })
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.xhtml',
                    {'section': 'images', 'image': image})
