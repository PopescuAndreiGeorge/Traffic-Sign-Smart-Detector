from SPARQLWrapper import SPARQLWrapper, JSON

TYPE                = 'type'
LABEL               = 'label'
CATEGORY            = 'subClassOf'
MEANING             = 'abstract'
LEGAL_REGULATION    = 'legalRegulation'
SHAPE               = 'P1419'
COLOR               = 'P462'
REMOVE_SPEED_LIMIT  = 'removesSpeedLimit'
HAS_SPEED_LIMIT     = 'hasSpeedLimit'
REMOVES_RESTRICTION = 'removesRestriction'
PRECEDE_BY          = 'isPrecededBy'
PRECEDE_SIGNS       = 'precedes'

label_mapper = {
  TYPE                : 'type',
  LABEL               : 'label',
  CATEGORY            : 'category',
  MEANING             : 'meaning',
  LEGAL_REGULATION    : 'legal_regulation',
  SHAPE               : 'shape',
  COLOR               : 'color',
  REMOVE_SPEED_LIMIT  : 'remove_speed_limit',
  HAS_SPEED_LIMIT     : 'has_speed_limit',
  REMOVES_RESTRICTION : 'removes_restrictions',
  PRECEDE_BY          : 'precede_by',
  PRECEDE_SIGNS       : 'precede_signs'
}

shapes_mapper = {
  'wd:Q19821'  : 'Triangular',
  'wd:Q17278'  : 'Cercular',
  'wd:Q164'    : 'Square',
  'wd:Q166080' : 'Octagon',
  'wd:Q40843'  : 'Cross',
}

colors_mapper = {
  'wd:Q3142'  : 'Red',
  'wd:Q943'   : 'Yellow',
  'wd:Q1088'  : 'Blue',
  'wd:Q23445' : 'Dark',
  'wd:Q3133'  : 'Green',
}


def get_sign_category(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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
    return ''
    

def get_sign_type(sign_name: str) -> str:
  try:

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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
    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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


def get_binding(binding: dict) -> str:
  return binding['property']['value'].split('#')[1] if '#' in binding['property']['value'] else binding['property']['value'].split('/')[-1]


def get_binding_value(binding: dict) -> str:
  return binding['object']['value'].split('#')[1] if '#' in binding['object']['value'] else binding['object']['value']



def get_sign_ontology_infos(sign_name: str) -> dict:
  result_infos = {
    label_mapper[TYPE]                : '',
    label_mapper[LABEL]               : '',
    label_mapper[CATEGORY]            : '',
    label_mapper[SHAPE]               : '',
    label_mapper[COLOR]               : '',
    label_mapper[REMOVE_SPEED_LIMIT]  : '',
    label_mapper[HAS_SPEED_LIMIT]     : '',
    label_mapper[MEANING]             : '',
    label_mapper[LEGAL_REGULATION]    : '',
    label_mapper[PRECEDE_BY]          : [],
    label_mapper[PRECEDE_SIGNS]       : [],
    label_mapper[REMOVES_RESTRICTION] : [],
  }

  dbpedia_links = {
    'ext_link_type'       : '',
    'ext_link_abstract'   : '',
    'ext_link_label'      : '',
    'ext_link_P1419'      : '',
    'ext_link_P462'       : '',
    'ext_link_color_ent'  : '',
    'ext_link_shape_ent'  : '',
    'ext_link_subClassOf' : '',
  }

  try:
    sparql = SPARQLWrapper("http://localhost:3030/TraS_Ontology/sparql")
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

      SELECT ?property ?object
      WHERE {{ 
        myowl:{sign_name} ?property ?object .
        FILTER (?object != owl:NamedIndividual)
        FILTER (?object != owl:Class)
      }}
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    sign_found = False

    for binding in results['results']['bindings']:
      label = get_binding(binding)
      value = get_binding_value(binding)

      if label not in label_mapper:
        continue
      
      sign_found = True
      key = label_mapper[label]

      if isinstance(result_infos[key], list):
        result_infos[key].append(value)
      else:
        result_infos[key] = value

      dbpedia_links['ext_link_' + label] = binding['property']['value']

    if result_infos[label_mapper[CATEGORY]] == '':
      result_infos[label_mapper[CATEGORY]] = get_sign_category(result_infos[TYPE])
      dbpedia_links['ext_link_subClassOf'] = 'http://www.w3.org/2000/01/rdf-schema#subClassOf'

    # TODO Cleanup
    dbpedia_links['ext_link_color_ent'] = f"http://www.wikidata.org/entity/{result_infos['color'][3:]}"
    dbpedia_links['ext_link_shape_ent'] = f"http://www.wikidata.org/entity/{result_infos['shape'][3:]}"

    result_infos['shape'] = get_sign_shape(sign_name)
    result_infos['color'] = get_sign_color(sign_name)

    return sign_found, result_infos, dbpedia_links
  
  except Exception as e:
    print(f'\n[ERROR] An error occurred: {e}\n')
    
    return result_infos


if __name__ == '__main__':

  # print(get_sign_ontology_infos("EndSpeedLimit100Sign"))

  # print(f'Infos: {get_sign_ontology_infos("EndSpeedLimit100Sign")}')
  # print(f'Infos: {get_sign_ontology_infos("StopSign")}')

  get_sign_ontology_infos("EndSpeedLimit100Sign")

