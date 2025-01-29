from SPARQLWrapper import SPARQLWrapper, JSON 

# <wdt:P1419 rdf:resource="wd:Q19821"/> triunghi
# <wdt:P1419 rdf:resource="wd:Q17278"/> cerc
# <wdt:P1419 rdf:resource="wd:Q164"/>   patrat
# <wdt:P462 rdf:resource="wd:Q3142"/>   red
# <wdt:P462 rdf:resource="wd:Q943"/>    yellow
# <wdt:P462 rdf:resource="wd:Q1088"/>   blue
# <wdt:P462 rdf:resource="wd:Q23445"/>  dark

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

    print(results)

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
   
if __name__ == '__main__':

  print(get_sign_removes_restriction("EndAllPreviouslySignedRestrictionsSign"))

