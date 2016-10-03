from django.shortcuts import render
from image.models import IMG
# Create your views here.


def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
                img=request.FILES.get('img')
                )
        new_img.save()
    return render(request, 'image/uploadimg.html')

def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'image/showimg.html', content)

