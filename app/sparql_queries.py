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
    return "Work in progress..."
