# Proposta Inicial do Jogo

## Nome provisório do jogo
Cosmic Dodge

## Integrantes do grupo
- Luiz
- Diego
- Thiago

## Tipo de jogo
Jogo de desviar de obstáculos (nave desviando de meteoros)

## Descrição geral
O jogador controla uma nave espacial posicionada na parte inferior da tela. Meteoros de diferentes níveis caem continuamente do topo da tela em posições e velocidades variadas. O objetivo é sobreviver o máximo de tempo possível desviando dos meteoros, acumulando pontos e tentando superar o recorde salvo.

## Objetivo do jogador
Sobreviver o maior tempo possível desviando dos meteoros, acumulando a maior pontuação e superando o recorde anterior.

## Regras principais
- A nave se move horizontalmente (esquerda e direita) pela parte inferior da tela.
- Meteoros surgem aleatoriamente no topo da tela e caem em direção à parte inferior.
- Existem três níveis de meteoros:
  - **Nível 1:** pequeno, cinza, velocidade baixa — vale 1 ponto ao desviar.
  - **Nível 2:** médio, laranja, velocidade média — vale 2 pontos ao desviar.
  - **Nível 3:** grande, vermelho, velocidade alta — vale 3 pontos ao desviar.
- No início do jogo, apenas meteoros de nível 1 aparecem. Conforme a pontuação aumenta, meteoros de nível 2 e 3 passam a surgir progressivamente.
- O jogador começa com 3 vidas. Cada colisão com um meteoro remove uma vida.
- Meteoros que saem da tela pela parte inferior sem atingir a nave não causam dano.
- O jogo encerra quando o jogador perde todas as vidas.
- O recorde é salvo em arquivo e exibido na tela. Ao superar o recorde, o novo valor é salvo automaticamente.

## Condição de vitória
O jogo não possui uma condição de vitória definitiva — o objetivo é sobreviver o maior tempo possível e superar o próprio recorde.

## Condição de derrota ou encerramento
O jogo encerra quando o jogador perde as 3 vidas ao colidir com meteoros. Uma tela de Game Over é exibida com a pontuação final e o recorde atual.

## Elementos previstos
- Nave do jogador (representada por um triângulo ou retângulo colorido)
- Meteoros de três níveis (tamanhos e cores diferentes: cinza, laranja e vermelho)
- Placar de pontuação na tela
- Indicador de vidas restantes
- Exibição do recorde salvo
- Tela de Game Over com pontuação final
- Tela inicial simples com instruções básicas

## Controles previstos
| Tecla | Ação |
|-------|------|
| ← (seta esquerda) | Mover a nave para a esquerda |
| → (seta direita) | Mover a nave para a direita |
| ESC | Encerrar o jogo |
| ENTER | Iniciar ou reiniciar o jogo |

## Estruturas de dados que poderão ser utilizadas
- **Listas:** armazenar os meteoros ativos na tela, cada um como um dicionário com seus atributos.
- **Dicionários:** representar cada meteoro com seus dados (posição x, posição y, nível, velocidade, tamanho, cor, pontos).
- **Tuplas:** representar cores RGB e dimensões fixas dos elementos visuais.
- **Variáveis simples:** pontuação atual, número de vidas, recorde, velocidade base.

Exemplo de estrutura de um meteoro:
```python
meteoro = {
    "x": 150,
    "y": 0,
    "nivel": 2,
    "velocidade": 4,
    "tamanho": 25,
    "cor": (255, 140, 0),
    "pontos": 2
}
```

## Uso previsto de arquivos
- Arquivo `data/recorde.txt`: armazena a maior pontuação já registrada.
- O recorde é lido ao iniciar o jogo e atualizado automaticamente ao ser superado.
- Possível uso de arquivo `data/config.txt` para armazenar configurações básicas, como velocidade inicial e quantidade de vidas.

## Testes planejados
- Teste da função de geração de meteoros: verificar se os atributos gerados estão dentro dos valores esperados para cada nível.
- Teste da função de colisão: verificar se a detecção de colisão entre a nave e os meteoros funciona corretamente.
- Teste da função de leitura e escrita do recorde: verificar se o arquivo é lido e salvo corretamente, inclusive em caso de arquivo inexistente.
- Teste da função de atualização da pontuação: verificar se os pontos são somados corretamente conforme o nível do meteoro desviado.
- Teste da lógica de progressão de dificuldade: verificar se os meteoros de nível 2 e 3 passam a aparecer nos momentos corretos.

## Principais dificuldades esperadas
- Implementar a detecção de colisão de forma precisa entre a nave e os meteoros.
- Controlar a geração aleatória dos meteoros de forma equilibrada para que o jogo seja desafiador, mas jogável.
- Gerenciar a progressão de dificuldade sem tornar o jogo impossível nos primeiros momentos.
- Organizar o código em funções e módulos de forma clara desde o início.
- Garantir que a leitura e escrita do arquivo de recorde funcione sem erros, inclusive na primeira execução.

## Escopo mínimo para a entrega final
- Janela do Pygame funcionando com loop principal.
- Nave controlável pelo teclado (esquerda e direita).
- Meteoros dos três níveis caindo com velocidades e tamanhos diferentes.
- Sistema de pontuação e vidas funcionando.
- Detecção de colisão entre nave e meteoros.
- Tela de Game Over com pontuação final.
- Leitura e salvamento do recorde em arquivo.
- Código organizado em funções.
- Testes básicos implementados.
- README e proposta preenchidos.
