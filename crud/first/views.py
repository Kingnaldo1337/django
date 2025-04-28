from django.shortcuts import render, redirect, get_object_or_404
from .models import carros
from django.http import HttpResponse


def cadastrar_carro(request):
    if request.method == 'GET':
        modelos = carros.objects.all()
        return render(request, 'index.html', {'carros': modelos})
    elif request.method == 'POST':
        modelo = request.POST.get('modelo')
        preco =  request.POST.get('preco')

    carro = carros(
        modelo= modelo,
        preco = preco,
    )

    carro.save()

    return redirect ('cadastrar_carro')

def deletar_carro(request, id):
    carro = get_object_or_404(carros, id=id)
    carro.delete()

    return redirect('cadastrar_carro')

def atualizar_carro(request, id):
    carro = get_object_or_404(carros, id=id)

    modelo = request.POST.get('modelo')
    preco =  request.POST.get('preco')
    
    carro.modelo = modelo
    carro.preco = preco
    carro.save()

    return redirect ('cadastrar_carro')