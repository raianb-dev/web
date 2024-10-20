from django.shortcuts import render, redirect
import re
from django.views.decorators.csrf import csrf_exempt
import requests

from website1.models import Event_click

def bot_page(request):
    return render(request,'bot.html')

def is_mobile_user_agent(user_agent):
    # Verifica se o user agent é de um dispositivo móvel
    mobile_user_agents = [
        "Mobile", "Android", "iPhone", "iPad", "iPod", "BlackBerry", 
        "Opera Mini", "IEMobile", "Windows Phone"
    ]
    return any(agent in user_agent for agent in mobile_user_agents)

def is_bot_user_agent(user_agent):
    # Lista de user agents de bots conhecidos
    bot_user_agents = [
        'facebookexternalhit', 'TikTokBot', 'Instagram', 
        'Googlebot', 'Bingbot', 'Facebot'
    ]
    return any(bot in user_agent for bot in bot_user_agents)

def redirect_get(request):
    # Verificar o user agent
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Detecção de bot
    if is_bot_user_agent(user_agent):
        return redirect('botpage')  # Redireciona para a página de bots

    # Verificar se é um usuário móvel
    is_mobile = is_mobile_user_agent(user_agent)

    # Redirecionar para a página correta com base no tipo de dispositivo
    if is_mobile:
        return render(request, 'pt.html')  # Renderiza a página para dispositivos móveis
    else:
        return render(request, 'web.html')  # Renderiza a página para desktop

    # Se nenhum dos casos acima se aplicar, renderize a página 404


def pixel(request):
    return render(request, 'pixel.html')

def pixel2(request):
    return render(request, 'pixel2.html')
@csrf_exempt
def redirect_monro(request):
    if request.method == "POST":
        email = request.POST.get('email')
        button = request.POST.get('button')
        full_name = request.POST.get('full_name')
        
        # Capturar IP
        ip = request.META.get('REMOTE_ADDR')
        
        # Capturar User-Agent
        user_agent = request.META.get('HTTP_USER_AGENT')

        # Capturar URL anterior (se necessário)
        history_href = request.META.get('HTTP_REFERER', 'unknown')

        # Geolocalização baseada no IP
        geo_ip = "Desconhecido"
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}')
            geo_ip = response.json().get('city', 'Desconhecido')
        except:
            pass

        # Criar e salvar o evento no banco de dados
        Event_click.objects.create(
            email=email,
            geo_ip=geo_ip,
            ip=ip,
            history_href=history_href,
            user_agent=user_agent,
            button = button,
            full_name = full_name
        )

        # Redirecionar o usuário para o link de promoção
        return render(request,'pixel.html')
