from django.shortcuts import render

def home(request):
	return render(request, 'welcome/home.html', {'title':'HOME'})

def products(request):
	return render(request, 'welcome/products.html', {'title':'PRODUCTS'})

def animals(request):
	return render(request, 'welcome/animals.html', {'title':'ANIMALS'})

def culture(request):
	return render(request, 'welcome/culture.html', {'title':'CULTURE'})

def bulls(request):
	return render(request, 'welcome/bulls.html', {'title':'KANGEYAM BULLS'})

def trees(request):
	return render(request, 'welcome/trees.html', {'title':'TREES'})

def plants(request):
	return render(request, 'welcome/plants.html', {'title':'PLANTS'})

def flowers(request):
	return render(request, 'welcome/flowers.html', {'title':'FLOWERS'})

def lectures(request):
	return render(request, 'welcome/flowers.html', {'title':'LECTURES'})

def fertilizers(request):
	return render(request, 'welcome/flowers.html', {'title':'ORGANIC FERTILIZERS'})

