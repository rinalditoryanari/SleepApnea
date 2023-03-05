from django.shortcuts import render


def features_activities(request):
    return render(request, 'pages/features-activities.html')


def features_post_create(request):
    return render(request, 'pages/features-post-create.html')


def features_post(request):
    return render(request, 'pages/features-post.html')


def features_profile(request):
    return render(request, 'pages/features-profile.html')


def features_settings(request):
    return render(request, 'pages/features-settings.html')


def features_setting_detail(request):
    return render(request, 'pages/features-setting-detail.html')


def features_tickets(request):
    return render(request, 'pages/features-tickets.html')
