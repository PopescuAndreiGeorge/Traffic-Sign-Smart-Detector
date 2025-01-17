from SPARQLWrapper import SPARQLWrapper, JSON  # pip install SPARQLWrapper

def test_query():
    sparql = SPARQLWrapper("http://localhost:3030/TraS_Dataset/sparql")
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT * WHERE {
      ?sub ?pred ?obj .
    } LIMIT 10
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def get_sign_info(sign_name: str):
    
    sign_name = sign_name[0].upper() + sign_name[1:]
    
    sparql = SPARQLWrapper("http://localhost:3030/TraS_Dataset/sparql")
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX : <http://ontology.asam.net/ontologies/Domain#>

    SELECT ?comment WHERE {{ :{sign_name} rdfs:comment ?comment . }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

