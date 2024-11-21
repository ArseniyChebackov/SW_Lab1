from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import FOAF, RDF, XSD
from rdflib.tools.rdf2dot import rdf2dot
import graphviz

g = Graph()
EX = Namespace("http://example.org/")

# Додавання інформації про Кейда
keid = EX.Keid
g.add((keid, RDF.type, FOAF.Person))
g.add((keid, FOAF.name, Literal("Keid")))
g.add((keid, FOAF.mbox, Literal("keid@example.org")))
g.add((keid, FOAF.based_near, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
g.add((keid, FOAF.degree, Literal("Bachelor of Biology", datatype=XSD.string)))
g.add((keid, FOAF.interest, Literal("birds")))
g.add((keid, FOAF.interest, Literal("ecology")))
g.add((keid, FOAF.interest, Literal("environment")))
g.add((keid, FOAF.interest, Literal("photography")))
g.add((keid, FOAF.interest, Literal("travel")))
g.add((keid, FOAF.visited, Literal("Canada")))
g.add((keid, FOAF.visited, Literal("France")))

# Додавання інформації про Емму
emma = EX.Emma
g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, FOAF.mbox, Literal("emma@example.org")))
g.add((emma, FOAF.based_near, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))
g.add((emma, FOAF.degree, Literal("Master of Chemistry", datatype=XSD.string)))
g.add((emma, FOAF.interest, Literal("cycling")))
g.add((emma, FOAF.interest, Literal("music")))
g.add((emma, FOAF.interest, Literal("travel")))
g.add((emma, FOAF.visited, Literal("Portugal")))
g.add((emma, FOAF.visited, Literal("Italy")))
g.add((emma, FOAF.visited, Literal("France")))
g.add((emma, FOAF.visited, Literal("Germany")))
g.add((emma, FOAF.visited, Literal("Denmark")))
g.add((emma, FOAF.visited, Literal("Sweden")))

# Додавання інформації про зустріч Кейда та Емми
g.add((keid, FOAF.knows, emma))
g.add((keid, FOAF.meetingPlace, Literal("Paris")))
g.add((keid, FOAF.meetingDate, Literal("2014-08", datatype=XSD.gYearMonth)))

# Візуалізація графу
def visualize_graph(g):
    stream = graphviz.Digraph()
    rdf2dot(g, stream)
    stream.render('graph', format='png', view=True)

visualize_graph(g)

# Серіалізація графу у формат TURTLE
turtle_data = g.serialize(format='turtle')
with open('graph.ttl', 'w') as f:
    f.write(turtle_data)

# Внесення змін до графу
g.add((keid, FOAF.visited, Literal("Germany")))
g.add((emma, FOAF.age, Literal(36, datatype=XSD.integer)))

# Збереження оновленого графу у форматі TURTLE
turtle_data = g.serialize(format='turtle')
with open('graph_updated.ttl', 'w') as f:
    f.write(turtle_data)

# Виведення всіх трійок на консоль
print("Всі трійки графу:")
for s, p, o in g:
    print(f"{s} {p} {o}")

# Виведення трійок, що стосуються лише про Емму
emma_query = """
PREFIX ex: <http://example.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?s ?p ?o
WHERE {
    ex:Emma ?p ?o .
}
"""

print("\nТрійки, що стосуються лише про Емму:")
emma_results = g.query(emma_query)
for row in emma_results:
    print(f"{row.s} {row.p} {row.o}")

# Виведення трійок, що містять імена людей
names_query = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?s ?p ?o
WHERE {
    ?s ?p ?o .
    FILTER(STRSTARTS(STR(?p), STR(foaf:name)))
}
"""

print("\nТрійки, що містять імена людей:")
names_results = g.query(names_query)
for row in names_results:
    print(f"{row.s} {row.p} {row.o}")