from django.contrib import messages
from django.shortcuts import render

from .models import Candidate


def applicant(request):
    if request.method == 'POST':
        try:
            nom = request.POST.get('nom')
            prenoms = request.POST.get('prenoms')
            email = request.POST.get('email')
            poste = request.POST.get('poste')
            portfolio_cv = request.FILES.get('portfolio_cv')

            new_applicant = Candidate(
                nom=nom,
                prenoms=prenoms,
                email=email,
                poste=poste,
                portfolio_cv=portfolio_cv)
            new_applicant.save()

            messages.success(request, 'Votre demande a été envoyée avec succès.')
        except Exception as e:
            messages.warning(request,
                             f'Une erreur inconnue s’est produite, veuillez nous contacter d’une autre manière. Détails de l’erreur: {e}')

    return render(request, 'home/forms.html', )


def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            new_message = Candidate(
                name=name,
                email=email,
                message=message)

            new_message.save()

            messages.success(request, 'Votre demande a été envoyée avec succès.')
        except Exception as e:
            messages.warning(request,
                             f'Une erreur inconnue s’est produite, veuillez nous contacter d’une autre manière. Détails de l’erreur: {e}')

    return render(request, 'home/contact.html', )


def contact_offre(request):
    return render(request, 'simple/home/contact-offre.html')
