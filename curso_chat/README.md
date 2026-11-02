# Gerador de Requisitos Multi-Agente

Este projeto utiliza inteligência artificial e uma arquitetura multi-agentes para automatizar a criação de Documentos de Requisitos Técnicos a partir de transcrições de reuniões comerciais. Desenvolvido para otimizar o fluxo de trabalho da Empresa Júnior e reduzir o tempo de documentação.

---

## Funcionalidades

* **Extração Inteligente:** Filtra conversas paralelas e identifica diretamente as dores de negócio e os objetivos reais do cliente.
* **Tradução Técnica:** Converte linguagem de negócios solta em Requisitos Funcionais e Não-Funcionais estruturados.
* **Validação de Escopo:** Analisa os requisitos gerados criticamente em busca de lacunas lógicas ou informações ausentes no pedido do cliente.
* **Formatação Automática:** Consolida os dados validados em um template oficial padronizado (Markdown ou JSON).

## Arquitetura de Agentes

O sistema opera como uma equipe de software autônoma orquestrada pelo CrewAI, composta por 4 agentes especialistas:

1. **Agente Analista (O Filtro):** Processa o arquivo `.txt` da reunião e extrai o escopo principal do projeto.
2. **Agente de Requisitos (O Tradutor):** Mapeia o escopo entregue pelo Analista em requisitos técnicos detalhados e categorizados.
3. **Agente Product Manager (O Revisor):** Critica a solução técnica e aponta falhas, dependências ou inconsistências.
4. **Agente Documentador (O Formatador):** Recebe a validação do PM e gera o documento final pronto para entrega.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Orquestração de Agentes:** CrewAI
* **Modelos de Linguagem (LLMs):** OpenAI (GPT-4o / GPT-4o-mini) ou Anthropic (Claude 3.5 Sonnet)
* **Ambiente:** `python-dotenv` para gerenciamento seguro de chaves de API

---
