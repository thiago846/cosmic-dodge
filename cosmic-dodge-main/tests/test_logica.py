import pygame
from src.funcoes import (
    calcular_pontos, jogador_perdeu, limitar_valor,
    verificar_colisao, tomar_dano,
)
from src.dados import atualizar_ranking


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_tomar_dano_reduz_vidas():
    """Deve reduzir a quantidade de vidas pelo valor de dano informado."""
    assert tomar_dano(3, 1) == 2


def test_verificar_colisao_quando_retangulos_se_sobrepoem():
    """Deve retornar True quando dois retângulos se sobrepõem."""
    nave = pygame.Rect(100, 100, 50, 30)
    meteoro = pygame.Rect(110, 110, 20, 20)
    assert verificar_colisao(nave, meteoro) is True


def test_verificar_colisao_quando_retangulos_nao_se_sobrepoem():
    """Deve retornar False quando os retângulos estão distantes."""
    nave = pygame.Rect(100, 100, 50, 30)
    meteoro = pygame.Rect(500, 500, 20, 20)
    assert verificar_colisao(nave, meteoro) is False


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_atualizar_ranking_ordena_do_maior_para_o_menor():
    """Deve inserir a nova pontuação e manter o ranking ordenado de forma decrescente."""
    ranking = [100, 80, 50]
    resultado = atualizar_ranking(ranking, 90)
    assert resultado == [100, 90, 80, 50]


def test_atualizar_ranking_mantem_apenas_top_5():
    """Deve manter apenas as 5 melhores pontuações no ranking."""
    ranking = [500, 400, 300, 200, 100]
    resultado = atualizar_ranking(ranking, 999)
    assert resultado == [999, 500, 400, 300, 200]
    assert len(resultado) == 5