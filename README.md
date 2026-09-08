# 🦈 SharkOlympics

Projeto desenvolvido para a disciplina de **Laboratório de Programação de Jogos** da **Universidade Federal Fluminense (UFF)**, no ano de **2023**.

## Sobre o projeto

SharkOlympics é um protótipo de jogo 2D em que o jogador controla um tubarão pela tela, feito em Python utilizando a biblioteca **PPlay**. O projeto foi construído como exercício prático dos conceitos vistos em aula, como criação de janelas, manipulação de sprites, captura de teclado e controle de estados de jogo (menu ↔ jogo).

## Tecnologias utilizadas

- **Python 3**
- **[PPlay](https://github.com/mafayaz/PPlay)** — biblioteca para desenvolvimento de jogos 2D em Python

## Como jogar

1. Instale as dependências (veja a seção [Instalação](#instalação)).
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```
3. No menu inicial:
   - Pressione **`A`** para entrar no jogo.
   - Pressione **`'`** (aspas simples) para fechar a janela.
4. Durante o jogo:
   - **Setas (↑ ↓ ← →)** — movimentam o tubarão pela tela.
   - **Espaço** — faz o tubarão avançar (dash) para a direita.
   - **ESC** — encerra a partida e retorna ao menu.

## Instalação

Clone o repositório e instale a biblioteca PPlay:

```bash
git clone <url-do-repositorio>
cd sharkolympics
pip install PPlay
```

Em seguida, rode o jogo com:

```bash
python main.py
```

## Estrutura do projeto

```
sharkolympics/
├── main.py       # Ponto de entrada — controla os estados do jogo (menu/jogo)
├── menu.py       # Tela de menu inicial
├── jogo.py       # Lógica principal do jogo (movimentação, colisão com bordas, salto)
├── fundo.png     # Imagem de fundo do jogo
├── tubarao padrao.png  # Sprite do personagem principal
└── *.psd         # Artes originais (Photoshop) usadas na criação dos sprites
```

## Status do projeto

Este é um trabalho acadêmico com fins didáticos, desenvolvido em um curto período de tempo como parte da disciplina. Por isso, o jogo está em estágio de **protótipo**: algumas mecânicas (como o "salto" do tubarão) e assets (como moedas, bomba, relógio e replay) foram planejados/esboçados, mas não chegaram a ser totalmente implementados ou integrados à versão final.

## Autoria

Trabalho acadêmico desenvolvido para a disciplina de Laboratório de Programação de Jogos — UFF (2023).
