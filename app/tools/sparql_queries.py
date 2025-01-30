from SPARQLWrapper import SPARQLWrapper, JSON 

shapes_mapper = {
  'wd:Q19821': 'Triangular',
  'wd:Q17278': 'Cercular',
  'wd:Q164': 'Square',
  'wd:Q166080': 'Octagon',
  'wd:Q40843': 'Cross',
}

colors_mapper = {
  'wd:Q3142': 'Red',
  'wd:Q943': 'Yellow',
  'wd:Q1088': 'Blue',
  'wd:Q23445': 'Dark',
  'wd:Q3133': 'Green',
}


def get_sign_category(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} rdfs:subClassOf ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    super_class = results['results']['bindings'][0]['object']['value'].split('#')[1]

    return super_class
  
  except:
    return 'No category'
    

def get_sign_type(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} dbo:label ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    type = results['results']['bindings'][0]['object']['value']

    return type
  
  except:
    return 'No type'


def get_sign_meaning(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} dbo:abstract ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    meaning = results['results']['bindings'][0]['object']['value']

    return meaning
  
  except:
    return ''


def get_sign_legal_regulation(sign_name: str) -> str:
  
  try:
    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} TrafficSign:legalRegulation ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    legal_regulation = results['results']['bindings'][0]['object']['value']

    return legal_regulation
  
  except:
    return ''


def get_sign_precede_by(sign_name: str) -> list[str]:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} TrafficSign:isPrecededBy ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    precede_signs = [result['object']['value'].split('#')[1] for result in results['results']['bindings']]

    return precede_signs
  
  except:
    return []


def get_sign_removes_restriction(sign_name: str) -> list[str]:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} TrafficSign:removesRestriction ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    removes_Restriction = [result['object']['value'].split('#')[1] for result in results['results']['bindings']]

    return removes_Restriction
  
  except:
    return []


def get_sign_precede_signs(sign_name: str) -> list[str]:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>

      SELECT ?object
      WHERE {{ myowl:{sign_name} myowl:precedes ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    precede_signs = [result['object']['value'].split('#')[1] for result in results['results']['bindings']]

    return precede_signs
  
  except:
    return []
   

def get_sign_shape(sign_name: str) -> str:	
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX wdt: <http://www.wikidata.org/prop/direct/>

      SELECT ?object
      WHERE {{ myowl:{sign_name} wdt:P1419 ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    shape = results['results']['bindings'][0]['object']['value']

    return shapes_mapper[shape]
  
  except:
    return 'No shape'


def get_sign_color(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX wdt: <http://www.wikidata.org/prop/direct/>

      SELECT ?object
      WHERE {{ myowl:{sign_name} wdt:P462 ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    color = results['results']['bindings'][0]['object']['value']

    return colors_mapper[color]
  
  except:
    return 'No color'

def get_sign_speed_limit(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS/sparql")
    query = f"""
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX db: <http://dbpedia.org/>
      PREFIX sd: <http://www.w3.org/ns/sparql-service-description#>
      PREFIX dbo: <http://dbpedia.org/property/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX myowl: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX TrafficSign: <http://www.semanticweb.org/nicol/ontologies/2025/0/TrafficSign#>
      PREFIX wdt: <http://www.wikidata.org/prop/direct/>

      SELECT ?object
      WHERE {{ myowl:{sign_name} TrafficSign:removesSpeedLimit ?object  }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    speed_limit = results['results']['bindings'][0]['object']['value']

    return speed_limit
  
  except:
    return ''


if __name__ == '__main__':

  print(get_sign_speed_limit("EndSpeedLimit100Sign"))
  print(get_sign_speed_limit("StopSign"))

