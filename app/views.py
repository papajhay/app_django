from django.http import HttpResponse
from django.utils.translation import get_language

def test_lang(request):
    return HttpResponse(f"LANG = {get_language()}")