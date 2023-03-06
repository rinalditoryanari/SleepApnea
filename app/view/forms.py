from django.shortcuts import render


def forms_advanced_form(request):
    return render(request, 'pages/stisla/forms/forms-advanced-form.html')


def forms_editor(request):
    return render(request, 'pages/stisla/forms/forms-editor.html')


def forms_validation(request):
    return render(request, 'pages/stisla/forms/forms-validation.html')
