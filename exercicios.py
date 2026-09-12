# Arquivo: exercicios.py - respostas dos exercicios da Aula 05
# Deve ficar na MESMA pasta de mapa.py e busca.py

# ---------------------------------------------------------------
# Exercicio 6 (resposta em texto, ate 5 linhas):
#
# "caminho + [vizinho]" cria uma lista NOVA a cada filho gerado; o
# caminho do no pai continua intacto e pode ser reaproveitado para
# gerar os outros irmaos. Ja "caminho.append(vizinho)" altera a
# MESMA lista que esta guardada na fronteira para varios itens (o
# pai e todos os seus filhos apontam para o mesmo objeto em memoria).
# Se usassemos append, cada vizinho novo seria colado nessa unica
# lista compartilhada, e todos os caminhos da fronteira acabariam
# reunidos numa lista so, cada vez mais longa e errada. A saida
# final nao mostraria o caminho correto ate o objetivo, e sim uma
# mistura de trechos de caminhos diferentes.
# ---------------------------------------------------------------
from mapa import mapa_romenia, grau, verifica_simetria
from busca import busca_generica


# ---------------------------------------------------------------
# Exercicio 4
# cidades_alcancaveis(grafo, inicio, k): cidades alcancaveis a
# partir de 'inicio' em no maximo k passos (uma "busca em largura"
# limitada por profundidade, sem se importar com o custo).
# ---------------------------------------------------------------
def cidades_alcancaveis(grafo, inicio, k):
    alcancadas = {inicio}          # conjunto: guarda o resultado
    fronteira_nivel = [inicio]     # lista: a "camada" atual da busca

    for _ in range(k):
        proxima_fronteira = []
        for cidade in fronteira_nivel:
            for vizinho, custo in grafo.get(cidade, []):
                if vizinho not in alcancadas:
                    alcancadas.add(vizinho)
                    proxima_fronteira.append(vizinho)
        fronteira_nivel = proxima_fronteira
        if not fronteira_nivel:   # nao ha mais para onde expandir
            break

    return alcancadas


if __name__ == '__main__':

    print('=== Exercicio 3: grau(grafo) ===')
    graus = grau(mapa_romenia)
    for cidade, n in sorted(graus.items()):
        print(f'{cidade:16} {n} vizinho(s)')

    maior = max(graus, key=graus.get)
    menor = min(graus, key=graus.get)
    print(f'\nCidade com MAIS estradas: {maior} ({graus[maior]} vizinhos)')
    print(f'Cidade(s) com MENOS estradas: {menor} ({graus[menor]} vizinhos)')
    # Como varios "becos sem saida" tem grau 1, mostramos todos eles:
    minimo = min(graus.values())
    empatados = sorted(c for c, n in graus.items() if n == minimo)
    print(f'Todas as cidades com grau minimo ({minimo}): {empatados}')

    print('\n=== Exercicio 4: cidades_alcancaveis ===')
    resultado = cidades_alcancaveis(mapa_romenia, 'Arad', 2)
    print(f'A partir de Arad, em ate 2 passos: {sorted(resultado)}')

    print('\n=== Exercicio 5: verifica_simetria ===')
    problemas = verifica_simetria(mapa_romenia)
    if not problemas:
        print('O grafo esta simetrico: toda aresta tem volta com o mesmo '
              'custo.')
    else:
        print('Problemas encontrados:')
        for p in problemas:
            print(' -', p)

    print('\n=== Exercicio 7: contador de nos expandidos ===')
    caminho, custo = busca_generica(mapa_romenia, 'Arad', 'Bucharest')
    print(' -> '.join(caminho))
    print(f'{custo} km em {len(caminho) - 1} passos')
