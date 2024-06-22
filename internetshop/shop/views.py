from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('''
    <h1>Всякозин</h1>
    <a href='/'>Главная</a>
    <a href='/products'>Товары</a>
    <a href='/aboutas'>О нас</a>
    
    <div style='border: 1px black solid'>
        <h2>Кирпич</h2>
        <img src='https://www.stroyportal.ru/media/cache/companies/181706/yml_images/1903/6679668_image_large.jpg'>
        <p>Кирпич - лучший предмет для определения погоды</p>
    </div>
    ''')