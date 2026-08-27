from src.config.credentials import CLIENT
from src.request.dry_run import configure_and_execute_dry_run
from src.request.query_job import created_query_job
from src.request.information_costs import information_costs
from src.template.query import gerar_query_patents, print_campos_disponiveis, print_limites_disponiveis
from src.data.input_limit import input_limit
from src.data.input_filters import input_filters

# Este é o ponto de entrada do programa. Ele executa a consulta, salva os resultados e exibe as informações de custo.
if __name__ == "__main__":
    #1. Imprimi na tela do usuário os campos disponiveis
    print_campos_disponiveis()
    #2. Solicita ao usuário os campos desejados
    campos_desejados = input("Digite os campos desejados, separados por vírgula: ").split(",")
    campos_desejados = [campo.strip() for campo in campos_desejados]
    print_limites_disponiveis()
    limite = input_limit()
    
    # 2.1 Solicita os filtros ao usuário
    filtros = input_filters()
    
    # 3. Gera a query com base nos campos desejados, no limite informado e nos filtros
    query,campos_por_fonte = gerar_query_patents(campos_desejados, limit=limite, filters=filtros)
    
    print(query)

    configure_and_execute_dry_run(query, CLIENT)
    print("Deseja prosseguir com a execução da consulta? (s/n)")
    proceed = input().lower()
    if proceed != 's':
        print("Consulta cancelada pelo usuário.")
        exit()
    query_job = created_query_job(query, CLIENT, arq='bq_patents_citations',campos_por_fonte=campos_por_fonte)
    information_costs(query_job)
    print("Dados salvos com sucesso!")    