def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0


def carregar_ranking(caminho_arquivo):
    """Carrega a lista de pontuações do ranking, ordenada da maior para a menor."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            pontuacoes = [int(linha.strip()) for linha in linhas if linha.strip() != ""]
            return sorted(pontuacoes, reverse=True)
    except FileNotFoundError:
        return []


def salvar_ranking(caminho_arquivo, ranking):
    """Salva a lista de pontuações do ranking em arquivo, uma por linha."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for pontuacao in ranking:
            arquivo.write(f"{pontuacao}\n")


def atualizar_ranking(ranking, nova_pontuacao, limite=5):
    """Insere uma nova pontuação no ranking, mantendo apenas as `limite` melhores."""
    ranking_atualizado = ranking + [nova_pontuacao]
    ranking_atualizado = sorted(ranking_atualizado, reverse=True)
    return ranking_atualizado[:limite]