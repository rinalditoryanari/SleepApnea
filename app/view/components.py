from django.shortcuts import render


def components_article(request):
    return render(request, 'pages/components-article.html')


def components_avatar(request):
    return render(request, 'pages/components-avatar.html')


def components_chat_box(request):
    return render(request, 'pages/components-chat-box.html')


def components_empty_state(request):
    return render(request, 'pages/components-empty-state.html')


def components_gallery(request):
    return render(request, 'pages/components-gallery.html')


def components_hero(request):
    return render(request, 'pages/components-hero.html')


def components_multiple_upload(request):
    return render(request, 'pages/components-multiple-upload.html')


def components_pricing(request):
    return render(request, 'pages/components-pricing.html')


def components_statistic(request):
    return render(request, 'pages/components-statistic.html')


def components_tab(request):
    return render(request, 'pages/components-tab.html')


def components_table(request):
    return render(request, 'pages/components-table.html')


def components_user(request):
    return render(request, 'pages/components-user.html')


def components_wizard(request):
    return render(request, 'pages/components-wizard.html')
