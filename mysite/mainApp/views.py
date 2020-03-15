from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {
        'contacts': ['Phone number: +7(920)179-90-33',
                     'GitHub Profile: https://github.com/JesterI3D',
                     'VK Profile: https://vk.com/jens1959',
                     'Gmail: montes3550@gmail.com']})


def more(request):
    return render(request, 'mainApp/more.html')
