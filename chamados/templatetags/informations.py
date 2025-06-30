from django import template
from chamados.models import Chamado

register = template.Library()

@register.inclusion_tag('partials/informations.html')
def render_informations():
    total_chamados = Chamado.objects.count()
    em_andamento = Chamado.objects.filter(status='em_andamento').count()
    a_fazer = Chamado.objects.filter(status='aberto').count()
    resolvidos = Chamado.objects.filter(status='resolvido').count()

    return {
        'total_chamados': total_chamados,
        'em_andamento': em_andamento,
        'a_fazer': a_fazer,
        'resolvidos': resolvidos,
    }