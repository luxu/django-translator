from django.shortcuts import render
from translate import Translator

def home(request):
    template_name = "app/home.html"
    if request.method == "GET":
        return render(request, template_name)
    text = request.POST["translate"]
    to_lang = request.POST["tolanguage"]
    from_lang = request.POST["fromlanguage"]
    translator = Translator(to_lang=to_lang, from_lang=from_lang)
    translation = translator.translate(text)

    context = {
        "translation": translation,
    }
    return render(request, template_name, context)
