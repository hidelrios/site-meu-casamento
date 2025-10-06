from django.shortcuts import render, redirect, get_object_or_404
from .models import Presente
from convidados.models import Convidado

def lista_presentes(request):
    presentes = Presente.objects.all()
    return render(request, "presentes/lista.html", {"presentes": presentes})


def reservar_presente(request, presente_id):
    presente = get_object_or_404(Presente, id=presente_id)

    convidado_id = request.session.get("convidado_id")
    convidado = None
    if convidado_id:
        convidado = Convidado.objects.get(id=convidado_id)

    if not presente.reservado:
        # Aqui basta reservar imediatamente ao clicar
        nome = convidado.nome if convidado else "Convidado"
        presente.reservado = True
        presente.reservado_por = nome
        presente.save()
        # Redireciona para a página de agradecimento
        return redirect("pagina_agradecimento")

    return redirect("lista_presentes")


def pagina_agradecimento(request):
    return render(request, "presentes/agradecimento.html")