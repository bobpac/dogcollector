from django.shortcuts import render

dogs = [
  {'name': 'Bubba', 'breed': 'Bernese Mountain Dog', 'description': 'Solid as a rock', 'age': 4},
  {'name': 'Chi Chi', 'breed': 'Chiweene', 'description': 'Grumpy old man', 'age': 12},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })