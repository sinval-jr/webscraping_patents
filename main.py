from src.config.credentials import CLIENT
from src.request.dry_run import configure_and_execute_dry_run
from src.request.query_job import created_query_job
from src.request.information_costs import information_costs
from src.template.query import gerar_query_patents, print_campos_disponiveis, print_limites_disponiveis
from src.data.input_limit import input_limit

# Este é o ponto de entrada do programa. Ele executa a consulta, salva os resultados e exibe as informações de custo.
if __name__ == "__main__":
    print_campos_disponiveis()
    campos_desejados = input("Digite os campos desejados, separados por vírgula: ").split(",")
    campos_desejados = [campo.strip() for campo in campos_desejados]
    print_limites_disponiveis()
    limite = input_limit()
    query = gerar_query_patents(campos_desejados, limit=limite)
    
    print(query)
    #Antes criação da query
    configure_and_execute_dry_run(query, CLIENT)
    print("Deseja prosseguir com a execução da consulta? (s/n)")
    proceed = input().lower()
    if proceed != 's':
        print("Consulta cancelada pelo usuário.")
        exit()
    query_job = created_query_job(query, CLIENT, arq='bq_patents_citations')
    information_costs(query_job)
    print("Data saved to patents_data_citations.csv")    