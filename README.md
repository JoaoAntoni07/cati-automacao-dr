# cati-automacao-drs
Esse repositório é dedicado ao desenvolvimento da esteira de automação para extração e geração de Documentos de Requisitos de Software (DRS) para a CATI Jr.

## Objetivo:
- Repositório dedicado à automação do fluxo de engenharia de requisitos, integrando Google Drive, Google Apps Script e Agentes de IA (CrewAI + Claude) para gerar relatórios padronizados no gabarito AEP Aero a partir de transcrições de reuniões.

## Ferramentas utilizadas:
- Python
- FastAPI
- CrewAI
- Anthropic (Claude)
- Google Apps Script
- Localtunnel
- Uvicorn

## Estrutura do repositório:
- **README.md**: Documentação principal do projeto.
- **.gitignore**: Arquivo para ignorar arquivos sensíveis e ambientes virtuais (como `.env` e `.venv`).
- **requirements.txt**: Lista de dependências Python do projeto.
- **agentes.py**: Código principal contendo a API FastAPI e os agentes CrewAI configurados com o gabarito AEP Aero.
- **google_apps_script/**: Pasta contendo o `Codigo.gs` para integração automática com o Google Drive.  