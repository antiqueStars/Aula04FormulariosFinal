from django.shortcuts import render, redirect
from .models import Cantoras, NanoGames

# Create your views here.
def home(request):
  cantoras = Cantoras.objects.all()
  nanoGames = NanoGames.objects.all()
  print(cantoras)
  return render(request, "home.html", context={
    "Cantoras": cantoras,
    "NanoGame": nanoGames
  })

def create_cantoras(request,id):
  if request.method == "POST":
    Cantoras.objects.create(
      nome = request.POST['nome'],
      instrumento = request.POST['instrumento'],
      debut_date = request.POST['debut_date'],
    )

    return redirect("home")
  return render(request, "forms.html", context = {"action":"Adicionar"})

def update_cantoras(request,id):
  cantoras = Cantoras.objects.get(id=id)
  if request.method == "POST":
      cantoras.nome = request.POST['nome'],
      cantoras.instrumento = request.POST['instrumento']
      cantoras.debut_date = request.POST['debut_date']
      cantoras.save
    

      return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","cantoras": cantora})

def delete_cantoras(request, id):
  cantoras = Cantoras.objects.get(id=id)
  if request.method == "POST":
    if "confirm" in request.POST:
      cantoras.delete()

    return redirect("home")
  return render(request, "forms.html", context = {"cantoras" : cantora})

def create_nanoGames(request,id):
  if request.method == "POST":
    nanoGames.objects.create(
      name = request.POST['name'],
      release = request.POST['release'],
      platform = request.POST['platform'],
    )

    return redirect("home")
  return render(request, "forms.html", context = {"action":"Adicionar"})

def update_nanoGames(request,id):
  nanogames = nanoGames.objects.get(id=id)
  if request.method == "POST":
      nanoGames.name = request.POST['name'],
      nanoGames.release = request.POST['release']
      nanoGames.platform = request.POST['debut_date']
      nanoGames.save()
    

      return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","nanoGames": nanoGame})

def delete_cantoras(request, id):
  nanogames = nanoGames.objects.get(id=id)
  if request.method == "POST":
    if "confirm" in request.POST:
      nanogames.delete()

    return redirect("home")
  return render(request, "forms.html", context = {"nanoGames" : nanoGame})