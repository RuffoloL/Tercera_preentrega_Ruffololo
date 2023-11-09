from django.shortcuts import render

def saludo_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response
