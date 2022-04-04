from cmath import exp
from .models import Post,Category

def Categorys(request):
    try:
        category = Category.objects.all()
        return {'category':category}
    except Exception:
        category = ''
        return {'category':category}


def BlogPost(request):
    try:
        latest = Post.objects.all().filter(status="P")
        return {'latest':latest}
    except Exception:
        latest = ''
        return{'latest':latest}