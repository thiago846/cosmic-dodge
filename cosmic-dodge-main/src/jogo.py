import pygame
import random
from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    CINZA, BRANCO, PRETO, AMARELO, AZUL,
    CAMINHO_RECORDE, CAMINHO_RANKING, VELOCIDADE_NAVE, NIVEIS_METEORO,
)
from src.funcoes import (
    calcular_pontos, jogador_perdeu,
    limitar_valor, verificar_colisao, tomar_dano,
)
from src.dados import (
    salvar_recorde, carregar_recorde,
    carregar_ranking, salvar_ranking, atualizar_ranking,
)


class Player(pygame.sprite.Sprite):
    """Nave do jogador, desenhada com formas geométricas (sem imagem externa)."""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((64, 80), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.draw_ship()

    def draw_ship(self):
        # Corpo principal da nave
        pygame.draw.polygon(
            self.image, (80, 180, 255),
            [(32, 0), (58, 58), (32, 48), (6, 58)]
        )
        # Sombra interna
        pygame.draw.polygon(
            self.image, (20, 80, 150),
            [(32, 10), (48, 55), (32, 45), (16, 55)]
        )
        # Cockpit
        pygame.draw.ellipse(self.image, (180, 240, 255), (22, 18, 20, 26))
        # Asas
        pygame.draw.polygon(
            self.image, (40, 120, 220),
            [(6, 58), (0, 78), (24, 62)]
        )
        pygame.draw.polygon(
            self.image, (40, 120, 220),
            [(58, 58), (64, 78), (40, 62)]
        )
        # Propulsor
        pygame.draw.polygon(
            self.image, (255, 180, 40),
            [(24, 58), (32, 80), (40, 58)]
        )
        pygame.draw.polygon(
            self.image, (255, 80, 20),
            [(28, 60), (32, 74), (36, 60)]
        )
        # Brilho frontal
        pygame.draw.line(self.image, (220, 255, 255), (32, 4), (32, 44), 2)


def criar_meteoro():
    """Gera um meteoro aleatório com nível 1, 2 ou 3."""
    nivel = random.randint(1, 3)
    dados = NIVEIS_METEORO[nivel]
    return {
        "x": random.randint(0, LARGURA_TELA - dados["tamanho"] * 2),
        "y": -dados["tamanho"],
        "nivel": nivel,
        "velocidade": dados["velocidade"],
        "tamanho": dados["tamanho"],
        "cor": dados["cor"],
        "pontos": dados["pontos"],
    }


def desenhar_ranking(tela, fonte, ranking, x, y):
    """Desenha a lista do top 5 ranking na tela, a partir da posição (x, y)."""
    titulo = fonte.render("TOP 5:", True, AMARELO)
    tela.blit(titulo, (x, y))

    if not ranking:
        vazio = fonte.render("(ainda sem pontuações)", True, BRANCO)
        tela.blit(vazio, (x, y + 30))
        return

    for posicao, pontuacao in enumerate(ranking, start=1):
        linha = fonte.render(f"{posicao}. {pontuacao} pts", True, BRANCO)
        tela.blit(linha, (x, y + 30 * posicao))


def desenhar_tela_inicio(tela, fonte_grande, fonte_pequena, recorde, ranking):
    """Desenha a tela de início do jogo, com recorde e ranking."""
    tela.fill(CINZA)
    titulo = fonte_grande.render("COSMIC DODGE", True, AMARELO)
    instrucao = fonte_pequena.render("Pressione ENTER para jogar", True, BRANCO)
    rec = fonte_pequena.render(f"Recorde: {recorde}", True, AZUL)

    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 100))
    tela.blit(instrucao, (LARGURA_TELA // 2 - instrucao.get_width() // 2, 220))
    tela.blit(rec, (LARGURA_TELA // 2 - rec.get_width() // 2, 270))

    desenhar_ranking(tela, fonte_pequena, ranking, LARGURA_TELA // 2 - 80, 340)

    pygame.display.flip()


def desenhar_jogo(tela, jogador, meteoros, pontos, vidas, recorde, fonte):
    """Desenha todos os elementos do jogo na tela."""
    tela.fill(CINZA)
    tela.blit(jogador.image, jogador.rect)
    for m in meteoros:
        pygame.draw.circle(tela, m["cor"], (m["x"], m["y"]), m["tamanho"])
    hud = fonte.render(
        f"Pontos: {pontos}  Vidas: {vidas}  Recorde: {recorde}  (P = pausar)",
        True, BRANCO,
    )
    tela.blit(hud, (10, 10))
    pygame.display.flip()


def desenhar_pausa(tela, fonte_grande, fonte_pequena):
    """Desenha a tela de pausa sobre o jogo."""
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    overlay.set_alpha(180)
    overlay.fill(PRETO)
    tela.blit(overlay, (0, 0))

    msg = fonte_grande.render("PAUSADO", True, AMARELO)
    instrucao = fonte_pequena.render("Pressione P para continuar", True, BRANCO)
    tela.blit(msg, (LARGURA_TELA // 2 - msg.get_width() // 2, 230))
    tela.blit(instrucao, (LARGURA_TELA // 2 - instrucao.get_width() // 2, 310))
    pygame.display.flip()


def desenhar_game_over(tela, fonte_grande, fonte_pequena, pontos, recorde, ranking):
    """Desenha a tela de game over, com pontuação final e ranking atualizado."""
    tela.fill(CINZA)
    msg = fonte_grande.render("GAME OVER", True, (220, 50, 50))
    pts = fonte_pequena.render(f"Pontuação: {pontos}  |  Recorde: {recorde}", True, BRANCO)
    reiniciar = fonte_pequena.render("ENTER para jogar de novo  |  ESC para sair", True, AZUL)

    tela.blit(msg, (LARGURA_TELA // 2 - msg.get_width() // 2, 100))
    tela.blit(pts, (LARGURA_TELA // 2 - pts.get_width() // 2, 200))
    tela.blit(reiniciar, (LARGURA_TELA // 2 - reiniciar.get_width() // 2, 250))

    desenhar_ranking(tela, fonte_pequena, ranking, LARGURA_TELA // 2 - 80, 320)

    pygame.display.flip()


def executar_jogo():
    """Executa o loop principal do jogo."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    fonte_grande = pygame.font.SysFont(None, 72)
    fonte_pequena = pygame.font.SysFont(None, 32)
    fonte_hud = pygame.font.SysFont(None, 28)

    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)

    estado = "inicio"

    jogador = Player(LARGURA_TELA // 2, ALTURA_TELA - 60)
    meteoros = []
    pontos = 0
    vidas = 3
    contador_meteoro = 0

    rodando = True
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                if evento.key == pygame.K_RETURN:
                    if estado in ("inicio", "gameover"):
                        # Reinicia o jogo
                        jogador = Player(LARGURA_TELA // 2, ALTURA_TELA - 60)
                        meteoros = []
                        pontos = 0
                        vidas = 3
                        contador_meteoro = 0
                        estado = "jogando"

                if evento.key == pygame.K_p:
                    if estado == "jogando":
                        estado = "pausado"
                    elif estado == "pausado":
                        estado = "jogando"

        if estado == "inicio":
            desenhar_tela_inicio(tela, fonte_grande, fonte_pequena, recorde, ranking)

        elif estado == "pausado":
            desenhar_jogo(tela, jogador, meteoros, pontos, vidas, recorde, fonte_hud)
            desenhar_pausa(tela, fonte_grande, fonte_pequena)

        elif estado == "jogando":
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                jogador.rect.x -= VELOCIDADE_NAVE
            if teclas[pygame.K_RIGHT]:
                jogador.rect.x += VELOCIDADE_NAVE
            jogador.rect.x = limitar_valor(jogador.rect.x, 0, LARGURA_TELA - jogador.rect.width)

            # Gera meteoros em intervalos cada vez menores conforme a pontuação sobe
            contador_meteoro += 1
            intervalo_spawn = max(12, 40 - (pontos // 50))

            if contador_meteoro >= intervalo_spawn:
                meteoros.append(criar_meteoro())
                contador_meteoro = 0

            # Chuva especial de meteoros após 300 pontos, para aumentar o desafio
            if pontos > 300 and random.randint(1, 300) == 1:
                quantidade = random.randint(4, 8)
                for _ in range(quantidade):
                    meteoros.append(criar_meteoro())

            for m in meteoros:
                m["y"] += m["velocidade"]

            for m in meteoros[:]:
                if m["y"] > ALTURA_TELA + m["tamanho"]:
                    meteoros.remove(m)
                    pontos = calcular_pontos(pontos, m["pontos"])

            for m in meteoros[:]:
                rect_m = pygame.Rect(m["x"] - m["tamanho"], m["y"] - m["tamanho"],
                                     m["tamanho"] * 2, m["tamanho"] * 2)
                if verificar_colisao(jogador.rect, rect_m):
                    vidas = tomar_dano(vidas, 1)
                    meteoros.remove(m)

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(CAMINHO_RECORDE, recorde)

            if jogador_perdeu(vidas):
                ranking = atualizar_ranking(ranking, pontos)
                salvar_ranking(CAMINHO_RANKING, ranking)
                estado = "gameover"

            desenhar_jogo(tela, jogador, meteoros, pontos, vidas, recorde, fonte_hud)

        elif estado == "gameover":
            desenhar_game_over(tela, fonte_grande, fonte_pequena, pontos, recorde, ranking)

    pygame.quit()
