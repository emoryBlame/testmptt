from django.shortcuts import render
from .models import *
from .forms import ElemForm

# Create your views here.


def home(request, page = 1):
	template = 'index.html'
	page = int(page)
	groups = Group.objects.all()
	groups = groups[10*(page - 1): 10*page] #if page <= 10 else groups[10*page: 10*(page+1)] if groups.count()-10*page > 10 else groups[10*page:groups.count()]
	elements = Element.objects.all()
	div, mod = divmod(groups.count(), 10)
	npages = div + 1 if mod else div
	pages = [i for i in range(1, npages + 1)]
	
	return render(request, template, {'groups': groups, 'npages': npages, 'pages': pages})


def get_group(request, groupname):
	template = 'groups.html'
	group = Group.objects.get(name = groupname)
	childsGroup = Group.objects.filter(parent__name = group.name).order_by('name')
	childsElements = Element.objects.filter(parent__name = group.name).filter(checked = 1).order_by('name')

	return render(request, template, {"cG": childsGroup, 'cE': childsElements, 'group': group})


def addElem(request):
	template = 'add.html'
	if request.method == "POST":
		form = ElemForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			context = {"text": "Форма создана!"}
		else:
			context = {"form" : ElemForm(), "text": "Заполните форму корректно!"}
	else:
		context = {"form" : ElemForm(), "text": "Заполните форму"}

	return render(request, template, context)
