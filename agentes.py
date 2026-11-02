import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Agent, Task, Crew, LLM

# 1. Inicializa o aplicativo FastAPI
app = FastAPI(title="API de Requisitos - Empresa Júnior")

# 2. Define o formato do JSON que a API vai receber
class DocumentoEntrada(BaseModel):
    texto: str

# Configura o LLM do Claude
llm_claude = LLM(
    model="anthropic/claude-sonnet-5-5",
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# 3. Gabarito Institucional da AEP Aero
GABARITO_AEP_AERO = """
# Documento de Requisitos de Software (DRS) - [Nome do Projeto]

## 1. Visão Geral do Projeto
- **Objetivo do Sistema:** [Descrição clara do propósito principal]
- **Escopo:** [O que o sistema faz e o que está fora de escopo]

## 2. Requisitos Funcionais (RF)
| ID | Nome do Requisito | Descrição Detalhada | Prioridade (Alta/Média/Baixa) |
|---|---|---|---|
| RF-01 | Exemplo | O sistema deve permitir... | Alta |

## 3. Requisitos Não-Funcionais (RNF)
| ID | Categoria | Descrição | Critério de Aceite Mensurável |
|---|---|---|---|
| RNF-01 | Usabilidade/Desempenho | O tempo de resposta deve... | Resposta em < 2 segundos |

## 4. Regras de Negócio (RN)
- **RN-01:** [Regra ou restrição de negócio que condiciona as funcionalidades]

## 5. Premissas e Restrições
- [Premissas de tecnologia, integrações externas ou limitações de ambiente]
"""

# 4. Rota POST
@app.post("/gerar-requisitos")
def gerar_requisitos(doc: DocumentoEntrada):
    try:
        # Cria o agente especializado no padrão AEP Aero
        engenheiro = Agent(
            role='Engenheiro de Requisitos Sênior - Padrão AEP Aero',
            goal='Traduzir transcrições de reuniões em Documentos de Requisitos de Software estritamente no gabarito AEP Aero.',
            backstory='Você é um especialista em análise de negócios e engenharia de requisitos de software na Empresa Júnior. Sua prioridade máxima é a precisão técnica e a conformidade 100% com o gabarito institucional da AEP Aero.',
            llm=llm_claude,
            verbose=True
        )

        # Define a tarefa forçando a estrutura exata do gabarito no expected_output
        tarefa_extracao = Task(
            description=f'''Analise criteriosamente a transcrição da reunião abaixo e extraia todas as necessidades do cliente.

--- INÍCIO DA TRANSCRIÇÃO ---
{doc.texto}
--- FIM DA TRANSCRIÇÃO ---

Instruções de Preenchimento:
1. Mantenha a nomenclatura de IDs padronizada (RF-01, RF-02..., RNF-01..., RN-01...).
2. Classifique a prioridade de cada Requisito Funcional em Alta, Média ou Baixa.
3. Se algum ponto não for mencionado na reunião, infira de forma lógica baseando-se no contexto ou marque como "A definir com o cliente".''',

            expected_output=f'''Um documento em Markdown estruturado **EXATAMENTE** conforme o gabarito a seguir, sem alterar a ordem das seções ou os nomes dos cabeçalhos:

{GABARITO_AEP_AERO}''',
            agent=engenheiro
        )

        # Monta a equipe e executa
        crew = Crew(
            agents=[engenheiro],
            tasks=[tarefa_extracao]
        )

        resultado = crew.kickoff()
        
        # Retorna o resultado final como resposta da API
        return {"status": "sucesso", "documento_gerado": resultado.raw}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))