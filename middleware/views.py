from django.shortcuts import render, redirect

def custom_redirect(request, undefined_path):
    # Detectar o idioma original da URL
    original_language = 'pt' if request.path.startswith('/pt/') else 'ca' if request.path.startswith('/ca/') else None

    # Adicione condições para redirecionar com base no idioma original
    if original_language == 'pt' and not request.path.startswith('/pt/'):
        # Redirecione para a raiz da versão em portuguêsa
        return redirect(f'/pt/{undefined_path}')
    elif original_language == 'ca' and not request.path.startswith('/ca/'):
        # Redirecione para a raiz da versão em inglês
        return redirect(f'/ca/{undefined_path}')
    # Adicione mais condições conforme necessário

    # Se o idioma original não for detectado ou já estiver no caminho correto, renderize a página 404 personalizada
    return render(request, '404.html', {'path': request.path}, status=404)
