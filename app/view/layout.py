from django.shortcuts import render

# Create your views here.


def layout_default_layout(request):
    return render(request, 'pages/layout-default-layout.html')
