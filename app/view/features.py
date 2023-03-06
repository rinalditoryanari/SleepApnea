from django.shortcuts import render


def features_activities(request):
    return render(request, 'pages/stisla/features/features-activities.html')


def features_post_create(request):
    return render(request, 'pages/stisla/features/features-post-create.html')


def features_post(request):
    return render(request, 'pages/stisla/features/features-post.html')


def features_profile(request):
    return render(request, 'pages/stisla/features/features-profile.html')


def features_settings(request):
    return render(request, 'pages/stisla/features/features-settings.html')


def features_setting_detail(request):
    return render(request, 'pages/stisla/features/features-setting-detail.html')


def features_tickets(request):
    return render(request, 'pages/stisla/features/features-tickets.html')
