# -*- coding: utf-8 -*-

#Importando a biblioteca Elasticsearch

from elasticsearch import Elasticsearch as es 

es = Elasticsearch(hosts = ["http://localhost:9200"], 
                   basic_auth=("elastic", "nY5AQz37ZZIfMev9nY5AQz37ZZIfMev9")
                   
                   
                    )

print(es.info())

#curl -XGET "localhost:9200/_cluster/health?pretty"

#curl -XGET "localhost:9200/_cat/indices?v" 

#curl -XGET "localhost:9200/nome_do_indice/_search?pretty" -H 'Content-Type: application/json' -d'

