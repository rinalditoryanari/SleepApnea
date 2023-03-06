from django.shortcuts import render


def components_article(request):
    return render(request, 'pages/stisla/components/components-article.html')


def components_avatar(request):
    return render(request, 'pages/stisla/components/components-avatar.html')


def components_chat_box(request):
    return render(request, 'pages/stisla/components/components-chat-box.html')


def components_empty_state(request):
    return render(request, 'pages/stisla/components/components-empty-state.html')


def components_gallery(request):
    return render(request, 'pages/stisla/components/components-gallery.html')


def components_hero(request):
    return render(request, 'pages/stisla/components/components-hero.html')


def components_multiple_upload(request):
    return render(request, 'pages/stisla/components/components-multiple-upload.html')


def components_pricing(request):
    return render(request, 'pages/stisla/components/components-pricing.html')


def components_statistic(request):
    return render(request, 'pages/stisla/components/components-statistic.html')


def components_tab(request):
    return render(request, 'pages/stisla/components/components-tab.html')


def components_table(request):
    return render(request, 'pages/stisla/components/components-table.html')


def components_user(request):
    return render(request, 'pages/stisla/components/components-user.html')


def components_wizard(request):
    return render(request, 'pages/stisla/components/components-wizard.html')
