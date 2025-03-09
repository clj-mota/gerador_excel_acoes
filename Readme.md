# 📊 Gerador de Arquivos Excel com Dados de Ações

Este projeto busca dados históricos de uma ação no **Yahoo Finanças** e gera um arquivo **Excel** (`.xlsx`) com essas informações. Ideal para quem deseja acompanhar o desempenho de ativos ao longo do tempo.

## 🚀 Funcionalidades
- Busca dados de ações da bolsa pelo código (ex: `PETR4.SA`).
- Permite selecionar um período específico (ex: `2024-01-01` a `2024-03-01`).
- Gera um arquivo **Excel** automaticamente com os dados obtidos.

## 📋 Pré-requisitos

Antes de rodar o código, certifique-se de ter o Python instalado e as bibliotecas abaixo:

```sh
pip install yfinance pandas openpyxl
