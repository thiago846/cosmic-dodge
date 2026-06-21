# Cosmic Dodge

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Luiz
- Diego
- Thiago

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprite da nave e dados).
- `assets/`: imagens, fontes e sons (não utilizados na versão final — a nave é desenhada com formas geométricas).
- `data/`: arquivos persistentes (recorde).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial (`proposta.MD`).

## Descrição do jogo

O jogador controla uma nave espacial na parte inferior da tela. Meteoros de três níveis (pequeno/lento, médio/moderado e grande/rápido) caem continuamente do topo da tela em posições aleatórias. O objetivo é desviar dos meteoros o maior tempo possível, acumulando pontos e tentando superar o recorde salvo em arquivo.

Conforme a pontuação aumenta, os meteoros passam a aparecer com mais frequência, tornando o jogo progressivamente mais difícil. Após 300 pontos, há chance de ocorrer uma "chuva" repentina de vários meteoros ao mesmo tempo.

## Objetivo do jogador

Sobreviver o maior tempo possível desviando dos meteoros e fazer a maior pontuação, superando o recorde anterior salvo em `data/recorde.txt`.

## Regras do jogo

- A nave se move horizontalmente (esquerda e direita) na parte inferior da tela.
- Meteoros surgem aleatoriamente no topo da tela e caem em direção à parte inferior.
- Existem três níveis de meteoro:
  - **Nível 1:** pequeno, cinza, velocidade baixa — vale 1 ponto ao ser desviado.
  - **Nível 2:** médio, laranja, velocidade média — vale 2 pontos ao ser desviado.
  - **Nível 3:** grande, vermelho, velocidade alta — vale 3 pontos ao ser desviado.
- O jogador começa com 3 vidas. Cada colisão com um meteoro remove uma vida.
- A pontuação aumenta automaticamente quando um meteoro passa da nave sem colidir.
- Quanto maior a pontuação, menor o intervalo entre o surgimento de novos meteoros (dificuldade progressiva).
- Acima de 300 pontos, existe uma pequena chance, a cada quadro, de uma "chuva" de 4 a 8 meteoros surgirem de uma vez.
- O jogo pode ser pausado e despausado a qualquer momento durante a partida.
- O jogo termina quando o jogador perde as 3 vidas (Game Over).
- O recorde é salvo automaticamente em arquivo sempre que é superado.
- As 5 melhores pontuações de todas as partidas jogadas ficam salvas em um ranking (top 5), exibido na tela inicial e na tela de Game Over.

## Controles

- **Seta esquerda:** mover a nave para a esquerda
- **Seta direita:** mover a nave para a direita
- **P:** pausar / continuar a partida
- **ENTER:** iniciar o jogo / jogar novamente após o Game Over
- **ESC:** sair do jogo

## Conceitos da disciplina aplicados

- **Funções e modularização:** o código é dividido em funções com responsabilidades claras (`criar_meteoro`, `verificar_colisao`, `tomar_dano`, `calcular_pontos`, funções de desenho de cada tela).
- **Estruturas condicionais e laços de repetição:** controle dos estados do jogo (início, jogando, game over) e do loop principal.
- **Listas:** armazenamento dos meteoros ativos na tela e do ranking com as 5 melhores pontuações.
- **Dicionários:** cada meteoro é representado por um dicionário com seus atributos (posição, nível, velocidade, tamanho, cor, pontos).
- **Leitura e escrita em arquivo:** o recorde é lido ao iniciar o jogo e salvo automaticamente em `data/recorde.txt` sempre que é superado; o ranking (top 5) é lido e salvo em `data/ranking.txt` ao final de cada partida.
- **Programação orientada a objetos (classe):** a nave do jogador é implementada como uma classe (`Player`), herdando de `pygame.sprite.Sprite`.
- **Testes automatizados:** funções de lógica do jogo (pontuação, dano, colisão, derrota, limites de movimento) são testadas com `pytest`.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/thiago846/cosmic-dodge
cd cosmic-dodge
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Referências e assets externos

- O jogo não utiliza imagens, sons ou fontes externas na versão final. A nave do jogador é desenhada inteiramente em código, usando formas geométricas do Pygame (`pygame.draw.polygon`, `pygame.draw.ellipse`, `pygame.draw.line`).
- O arquivo `assets/imagens/spritesheet.bmp`, presente no template original da disciplina, não é utilizado na versão final do jogo.
- Estrutura de projeto baseada no template oficial da disciplina: [IntroAlgs_pygame_template](https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template).

## Principais desafios encontrados

- Ajustar a detecção de colisão entre a nave (retângulo) e os meteoros (círculos), aproximando o meteoro de um retângulo delimitador para reutilizar a função `colliderect` do Pygame.
- Equilibrar a curva de dificuldade para que o jogo comece acessível e fique desafiador sem ficar impossível rapidamente.
- Integrar o código desenvolvido por diferentes integrantes do grupo (nave desenhada como classe, lógica de dificuldade progressiva) em um único módulo coerente.
