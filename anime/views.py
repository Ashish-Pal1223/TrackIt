from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import animeForm
from .models import action, Romance, psychological

norm_form = animeForm()

# Create your views here.

def anime(request):
    if(request.method == "POST"):
        form = animeForm(request.POST)
        if form.is_valid():
            anime = request.POST["anime_name"]
            genre = request.POST["genre"]
            rating = request.POST["rating"]
            actions = request.POST["action"]
            if actions == "add" :
                if genre == "action" :
                    action.objects.create(title = anime, rating = rating)
                elif genre == "romance" :
                    Romance.objects.create(title = anime, rating = rating)
                else:
                    psychological.objects.create(title = anime, rating = rating)

                return HttpResponseRedirect(reverse("anime"))
            else:
                if genre == "action" :
                    anime_act = action.objects.get(title = anime)
                    anime_act.delete()
                elif genre == "romance" :
                    anime_rom = Romance.objects.get(title = anime)
                    anime_rom.delete()
                else:
                    anime_psych = psychological.objects.get(title = anime)
                    anime_psych.delete()
                return HttpResponseRedirect(reverse("anime"))     
        else:
            form = animeForm(request.POST)
            return render(request, "anime/anime.html", {
                "action_anime" : action.objects.all(),
                "romance_anime" : Romance.objects.all(),
                "psychological_anime" : psychological.objects.all(),
                "form" : form
            })
    else:
        return render(request, "anime/anime.html", {
            "action_anime" : action.objects.all(),
            "romance_anime" : Romance.objects.all(),
            "psychological_anime" : psychological.objects.all(),
            "form" : norm_form
        })
