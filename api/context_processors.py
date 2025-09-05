from .models import Author 

def author_context(request):
    if request.user.is_authenticated:
        try:
            return {'current_author':Author.objects.get(user=request.user)}
        except Author.DoesNotExist:
            return {'current_author':None}
    return {'current_author':None}