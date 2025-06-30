def filtrar_chamados(queryset, params):
    # Filtro via select (único campo "filtro")
    filtro = params.get('filtro')

    if filtro:
        if filtro == 'favorito':
            queryset = queryset.filter(favorito=True)

        elif filtro.startswith('prioridade_'):
            prioridade = filtro.replace('prioridade_', '')
            queryset = queryset.filter(prioridade=prioridade)

        elif filtro.startswith('status_'):
            status = filtro.replace('status_', '')
            queryset = queryset.filter(status=status)

    # Filtros via botões individuais
    favorito = params.get('favorito')
    if favorito == 'True':
        queryset = queryset.filter(favorito=True)

    prioridade = params.get('prioridade')
    if prioridade:
        queryset = queryset.filter(prioridade=prioridade)

    status = params.get('status')
    if status:
        queryset = queryset.filter(status=status)

    return queryset
