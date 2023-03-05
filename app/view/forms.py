from django.shortcuts import render


def forms_advanced_form(request):
    return render(request, 'pages/forms-advanced-form.html')


def forms_editor(request):
    return render(request, 'pages/forms-editor.html')


def forms_validation(request):
    return render(request, 'pages/forms-validation.html')
