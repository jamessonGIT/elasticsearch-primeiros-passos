
from elasticsearch import Elasticsearch
import json

#=================================Cria Conexão com ElasticSearch============================================
es = Elasticsearch(hosts = ["http://localhost:9200"], 
                   basic_auth=("elastic", "nY5AQz37ZZIfMev9nY5AQz37ZZIfMev9")
                              
                    )
es_status = es

#====================================Caminho do arquivo JSON==================================================

caminho_arquivo = "base_demo.json"

#=============================Abrir e carregar o conteúdo do arquivo JSON=====================================
with open(caminho_arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

#=====================================Criação do índice========================================================
index_name = "meu_indice"

# Criar índice (opcional, se não existir)
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

if isinstance(dados, list):
    for i, doc in enumerate(dados):
        es.index(index=index_name, id=i+1, document=doc)
else:
    # Se for um único objeto JSON
    es.index(index=index_name, document=dados)

print("Dados inseridos no Elasticsearch!")

# Busca simples (todos os documentos)
res = es.search(index=index_name, query={"match_all": {}})

# Exibir resultados
for hit in res["hits"]["hits"]:
    print(hit["_source"])


