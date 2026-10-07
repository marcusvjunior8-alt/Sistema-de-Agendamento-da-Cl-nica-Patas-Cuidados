# 🐾 Sistema de Agendamento - Patas & Cuidados

Este projeto é um sistema simples de agendamento e cálculo de orçamento via linha de comando (CLI) desenvolvido em Python para a clínica veterinária e petshop **Patas & Cuidados**.

---

## 📌 Funcionalidades

- **Coleta de Informações:** Cadastra os dados do cliente, nome do pet, espécie e o serviço desejado.
- **Desconto Fidelidade (Clube Pet):** Aplica automaticamente 15% de desconto sobre o valor base do serviço para clientes membros do clube.
- **Taxa de Manejo Especial:** Adiciona uma taxa fixa de R$ 10,00 para felinos (`gato`).
- **Resumo Financeiro:** Exibe o detalhamento claro com o preço base, descontos aplicados, taxas adicionais e o valor total final a ser pago.

---

## 🛠️ Regras de Negócio Implementadas

| Condição | Regra Aplicada |
| :--- | :--- |
| `Clube Pet == 'sim'` | Desconto de **15%** no valor base do serviço |
| `Espécie == 'gato'` | Adição de taxa de manejo no valor de **R$ 10,00** |

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Ter o **Python 3.x** instalado na sua máquina.

### Passo a passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SeuUsuario/Sistema-de-Agendamento-da-Cl-nica-Patas-Cuidados.git](https://github.com/SeuUsuario/Sistema-de-Agendamento-da-Cl-nica-Patas-Cuidados.git)