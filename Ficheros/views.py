from django.shortcuts import render

def saludo_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response



def listar_autos(request):
    contexto ={
        "autos" :[
            {"marca":"Fiat", "modelo":"Cronos", "año":2022},
            {"marca":"VW", "modelo":"Gol-Trend", "año":2017},
            {"marca":"Renault", "modelo":"Clio", "año":2005},
        ]
    }
    http_response = render(
        request=request,
        template_name='Ficheros/lista_autos.html',
        context=contexto,     
    )
    return http_response
