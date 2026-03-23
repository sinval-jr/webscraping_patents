

QUERY = '''
SELECT 
  t1.publication_number AS patente_principal, 
  citacao.publication_number AS patente_citada
FROM 
  `patents-public-data.google_patents_research.publications` AS t1,
  UNNEST(t1.cited_by) AS citacao 
LIMIT 1000
'''