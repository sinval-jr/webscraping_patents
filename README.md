# PIBIT – Extração de Dados de Patentes via Google BigQuery

## 📌 Sobre o Projeto

Projeto de Iniciação Tecnológica (PIBIT) voltado à **captura automatizada de dados de patentes de invenção** a partir do dataset público [Google Patents](https://patents.google.com/) disponível no **Google BigQuery**.

O script permite ao usuário selecionar campos específicos de interesse (título, resumo, classificações IPC, citações, inventores, etc.), montar consultas SQL dinâmicas, estimar o custo de processamento antes da execução e exportar os resultados em arquivos `.csv` organizados por categoria de dados.

### Objetivos

- Automatizar a extração de dados patentários do repositório público do Google Patents no BigQuery.
- Oferecer uma interface interativa via terminal para seleção de campos e limites de consulta.
- Separar os resultados em planilhas organizadas por fonte/categoria (dados gerais, citações, classificações, etc.).
- Estimar custos antes da execução real, evitando gastos desnecessários.

---

## 🔑 Configuração de Credenciais (Conta de Serviço Google Cloud)

Para utilizar o script, é necessário possuir uma **conta de serviço** no Google Cloud com acesso ao BigQuery.

### Passo a passo

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Crie um **projeto** (ou use um existente).
3. Ative a **API do BigQuery** no projeto:
   - Menu lateral → **APIs e Serviços** → **Biblioteca** → pesquise "BigQuery API" → **Ativar**.
4. Crie uma **Conta de Serviço**:
   - Menu lateral → **IAM e Admin** → **Contas de serviço** → **Criar conta de serviço**.
   - Dê um nome e conceda o papel **BigQuery User** (ou `roles/bigquery.user`).
5. Gere uma **chave JSON**:
   - Na conta de serviço criada, vá em **Chaves** → **Adicionar chave** → **Criar nova chave** → formato **JSON**.
   - Um arquivo `.json` será baixado automaticamente. **Guarde este arquivo com segurança.**
6. Crie o arquivo `.env` na raiz do projeto (use o `.env.example` como referência):

```env
SERVICE_ACCOUNT_KEY={"type":"service_account","project_id":"seu-projeto", ...}
```

> ⚠️ **Importante:** Cole o conteúdo **completo** do arquivo JSON da conta de serviço como valor da variável `SERVICE_ACCOUNT_KEY` (em uma única linha).

---

## 📥 Instalação do Git e Download do Repositório

### Instalando o Git (caso ainda não tenha)

#### Windows
1. Baixe o instalador em [git-scm.com/downloads](https://git-scm.com/downloads).
2. Execute o instalador e siga as opções padrão.
3. Após a instalação, abra o **Prompt de Comando** ou **PowerShell** e verifique:

```bash
git --version
```

#### Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt install git -y
```

#### macOS
```bash
brew install git
```

### Clonando o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/sinval-jr/webscraping_patents.git
```

Acesse a pasta do projeto:

```bash
cd webscraping_patents
```

---

## 📦 Instalação de Dependências

### Pré-requisitos

- **Python 3.12+** instalado ([python.org/downloads](https://www.python.org/downloads/))

### Criando ambiente virtual e instalando pacotes

1. Crie um ambiente virtual dentro da pasta `src/`:

```bash
cd src
python -m venv .venv
```

2. Ative o ambiente virtual:

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install google-cloud-bigquery google-cloud-bigquery-storage pandas python-dotenv
```

4. Retorne para a raiz do projeto:

```bash
cd ..
```

---

## ▶️ Utilização do Script

Execute o script principal a partir da **raiz do projeto**:

```bash
python main.py
```

O script é interativo e seguirá as seguintes etapas pelo terminal:

### 1ª Etapa – Seleção de campos

O sistema exibirá todos os campos disponíveis, organizados por categoria. Você deverá digitar os campos desejados **separados por vírgula**.

**Campos disponíveis por categoria:**

| Categoria | Campos |
|---|---|
| Tabela principal (t1) | `publication_number`, `application_number`, `country_code`, `kind_code`, `application_kind`, `application_number_formatted`, `pct_number`, `family_id`, `spif_publication_number`, `spif_application_number`, `publication_date`, `filing_data`, `grant_date`, `priority_date`, `inventor`, `assignee`, `entity_status`, `art_unit` |
| Título (title) | `title_text`, `title_language`, `title_truncated` |
| Resumo (abstract) | `abstract_text`, `abstract_language`, `abstract_truncated` |
| Reivindicações (claims) | `claims_text`, `claims_language`, `claims_truncated` |
| Reivindicações HTML (claims_html) | `claims_html_text`, `claims_html_language`, `claims_html_truncated` |
| Descrição (description) | `description_text`, `description_language`, `description_truncated` |
| Descrição HTML (description_html) | `description_html_text`, `description_html_language`, `description_html_truncated` |
| Prioridade (priority_claim) | `priority_publication_number`, `priority_application_number`, `priority_npl_text`, `priority_type`, `priority_category`, `priority_filing_date` |
| Inventores harmonizados (inventor_harmonized) | `inventor_harmonized_name`, `inventor_harmonized_country_code` |
| Titulares harmonizados (assignee_harmonized) | `assignee_harmonized_name`, `assignee_harmonized_country_code` |
| Examinador (examiner) | `examiner_name`, `examiner_department`, `examiner_level` |
| Classificação USPC (uspc) | `uspc_code`, `uspc_inventive`, `uspc_first`, `uspc_tree` |
| Classificação IPC (ipc) | `ipc_code`, `ipc_inventive`, `ipc_first`, `ipc_tree` |
| Classificação IPCR (ipcr) | `ipcr_code`, `ipcr_inventive`, `ipcr_first`, `ipcr_tree` |
| Classificação FI (fi) | `fi_code`, `fi_inventive`, `fi_first`, `fi_tree` |
| Classificação FTerm (fterm) | `ft_code`, `ft_inventive`, `ft_first`, `ft_tree` |
| Classificação Locarno (locarno) | `locarno_code`, `locarno_inventive`, `locarno_first`, `locarno_tree` |
| Citações (citation) | `citation_publication_number`, `citation_application_number`, `citation_npl_text`, `citation_type`, `citation_category`, `citation_filing_date` |
| Patentes pai (parent) | `parent_publication_number`, `parent_application_number`, `parent_npl_text`, `parent_type`, `parent_category`, `parent_filing_date` |
| Patentes filha (child) | `child_publication_number`, `child_application_number`, `child_npl_text`, `child_type`, `child_category`, `child_filing_date` |

**Exemplo de resposta:**

```
publication_number, title_text, abstract_text, ipc_code, inventor_harmonized_name
```

### 2ª Etapa – Limite de registros

O sistema solicitará que você escolha o limite máximo de patentes retornadas (não afeta o tamanho em GB da consulta, somente o processamento interno do computador. Vale ressaltar que o processamento é feito em partes, logo não irá travar sua máquina somente irá demorar até o download dos arquivos):

```
Opções:
1. Limite padrão (1000)
2. Limite padrão (5000)
3. Limite padrão (10000)
4. Sem limite (Todos os dados)
```

**Responda com:** `1`, `2`, `3` ou `4`.

### 3ª Etapa – Filtros de busca

O sistema solicitará filtros opcionais para refinar a consulta. Pressione **Enter** para pular qualquer filtro que não deseja utilizar.

Os filtros disponíveis são:

| Filtro | Descrição | Exemplo de entrada |
|---|---|---|
| Data de Prioridade | Data exata ou período (separado por `\|`) | `20200101` ou `20200101 \| 20210101` |
| Inventor | Nome (ou parte) do inventor | `Silva` |
| Código do País | Código ISO do país | `BR`, `US`, `JP` |
| Assignee (Titular) | Nome (ou parte) da empresa/titular | `Petrobras` |
| Código IPC | Classificação IPC (ou parte) | `A61K` |
| Número da Publicação | Número exato da publicação | `US-10234567-B2` |
| Termo na Descrição | Busca por termo no texto do resumo (abstract) | `solar energy` |
| Termo geral | Busca por termo no título **e** no resumo | `machine learning` |

> 💡 **Dica:** Todos os filtros de texto (inventor, assignee, IPC, abstract, termo geral) são **case-insensitive** — ou seja, `Solar Energy` e `solar energy` retornam os mesmos resultados.

### 4ª Etapa – Estimativa de custo (Dry Run)

O script executará uma simulação da consulta e mostrará a **estimativa de dados processados (em GB)**. Nenhum dado é consumido nesta etapa. Recomenda-se que este valor não ultrapasse o limite de 10GB. Lembrando que o Big Query libera 1 TB para usufruto por mês de forma gratuita

```
ESTIMATIVA DA CONSULTA: 0.5423 GB
```

### 5ª Etapa – Confirmação de execução

```
Deseja prosseguir com a execução da consulta? (s/n)
```

**Responda com:** `s` para executar ou `n` para cancelar.

---

## 📊 Estrutura das Planilhas de Saída

Após a execução, o script gera **um ou mais arquivos `.csv`** na raiz do projeto, separados por categoria de dados (fonte). Cada arquivo é nomeado com o padrão:

```
patent_{fonte}_{YYYYMMDD_HHMMSS}.csv
```

Os arquivos gerados correspondem diretamente às **fontes dos campos selecionados**. Por exemplo, se você selecionar campos da tabela principal (`t1`), do título (`title`) e de citações (`citation`), serão gerados 3 arquivos.

### Exemplo de arquivos gerados

| Arquivo | Conteúdo |
|---|---|
| `patent_t1_20260505_095129.csv` | Dados gerais da patente (número de publicação, datas, inventores, etc.) |
| `patent_title_20260505_095129.csv` | Textos de título das patentes |
| `patent_abstract_20260505_095129.csv` | Textos de resumo das patentes |
| `patent_claims_20260505_095129.csv` | Textos de reivindicações das patentes |
| `patent_description_20260505_095129.csv` | Textos de descrição das patentes |
| `patent_priority_claim_20260505_095129.csv` | Dados de prioridade das patentes |
| `patent_ipc_20260505_095129.csv` | Classificações IPC das patentes |
| `patent_uspc_20260505_095129.csv` | Classificações USPC das patentes |
| `patent_citation_20260505_095129.csv` | Dados de citações vinculadas às patentes |
| `patent_inventor_harmonized_20260505_095129.csv` | Inventores harmonizados |
| `patent_assignee_harmonized_20260505_095129.csv` | Titulares harmonizados |
| `patent_examiner_20260505_095129.csv` | Dados do examinador |
| `patent_parent_20260505_095129.csv` | Patentes pai (relacionamentos) |
| `patent_child_20260505_095129.csv` | Patentes filha (relacionamentos) |

> 📝 **Nota:** Somente os arquivos correspondentes às fontes dos campos selecionados serão gerados.

### Chave de relacionamento entre planilhas

Todas as planilhas secundárias (citações, classificações, inventores, etc.) incluem automaticamente a coluna `publication_number` como **chave primária**, permitindo o cruzamento (JOIN) com a planilha principal `patent_t1_*.csv`.

### Exemplo de estrutura – `patent_t1_*.csv`

| publication_number | application_number | country_code | filing_data | grant_date |
|---|---|---|---|---|
| US-10234567-B2 | US-15678901 | US | 20180315 | 20200401 |

### Exemplo de estrutura – `patent_citation_*.csv`

| publication_number | citation_publication_number | citation_application_number | citation_filling_date |
|---|---|---|---|
| US-10234567-B2 | US-9876543-A1 | US-14567890 | 20150612 |

---

## 📁 Estrutura do Projeto

```
webscraping_patents/
├── main.py                          # Ponto de entrada do script
├── .env                             # Credenciais (não versionado)
├── .env.example                     # Modelo de arquivo de credenciais
├── .gitignore
├── README.md
└── src/
    ├── config/
    │   ├── credentials.py           # Carrega credenciais do .env e cria o client BigQuery
    │   └── settings.py              # Configurações gerais (caminhos)
    ├── template/
    │   └── query.py                 # Mapeamento de campos e geração dinâmica de queries SQL
    ├── request/
    │   ├── dry_run.py               # Estimativa de custo (dry run)
    │   ├── query_job.py             # Execução real da consulta no BigQuery
    │   └── information_costs.py     # Exibição de custos pós-execução
    ├── data/
    │   ├── input_limit.py           # Seleção interativa do limite de registros
    │   ├── input_filters.py         # Seleção interativa de filtros de busca
    │   ├── load_data.py             # Processamento e salvamento dos resultados em CSV
    │   └── transformer.py           # Transformações auxiliares de dados
    └── filter/                      # (reservado para expansões futuras)
```

---

## 📄 Licença

Projeto acadêmico desenvolvido no âmbito do programa PIBIT na UFG.
