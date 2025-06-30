from django import template
from chamados.models import Chamado

register = template.Library()

@register.inclusion_tag('partials/filtros_chamados.html')
def render_filtros_chamados():
    prioridades = [p[0] for p in Chamado.PRIORIDADES]
    status = [s[0] for s in Chamado.STATUS]
    tempos = [
        ('24h', 'Últimas 24 horas'),
        ('7d', 'Última semana'),
        ('30d', 'Último mês'),
        ('90d', 'Últimos 3 meses'),
        ('365d', 'Último ano'),
    ]
    return {
        'prioridades': prioridades,
        'status': status,
        'tempos': tempos,
    }
