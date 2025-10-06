from django.shortcuts import render, redirect
from .forms import ConvidadoForm
from presentes.models import Presente

def confirmar_presenca(request):
    if request.method == "POST":
        form = ConvidadoForm(request.POST)
        if form.is_valid():
            convidado = form.save()
            request.session["convidado_id"] = convidado.id  # guarda na sessão
            presentes = Presente.objects.all()
            return render(
                request,
                "presentes/lista.html",
                {"presentes": presentes, "convidado": convidado}
            )
    else:
        form = ConvidadoForm()
    return render(request, "convidados/confirmar_presenca.html", {"form": form})

