from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, FOAF, XSD

# Створення графу RDF
g = Graph()

# Визначення просторів імен
EX = Namespace("http://example.org/")

# Додавання даних для Кейда
cade = URIRef(EX.Cade)
g.add((cade, RDF.type, FOAF.Person))
g.add((cade, FOAF.name, Literal("Cade")))
g.add((cade, FOAF.based_near, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
g.add((cade, EX.degree, Literal("Bachelor of Biology", lang="en")))
g.add((cade, EX.degreeYear, Literal(2011, datatype=XSD.gYear)))
g.add((cade, FOAF.interest, Literal("Birds")))
g.add((cade, FOAF.interest, Literal("Ecology")))
g.add((cade, FOAF.interest, Literal("Environment")))
g.add((cade, FOAF.interest, Literal("Photography")))
g.add((cade, FOAF.interest, Literal("Travel")))
g.add((cade, EX.visited, Literal("Canada")))
g.add((cade, EX.visited, Literal("France")))

# Додавання даних для Емми
emma = URIRef(EX.Emma)
g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, FOAF.based_near, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))
g.add((emma, EX.degree, Literal("Master of Chemistry", lang="en")))
g.add((emma, EX.degreeYear, Literal(2015, datatype=XSD.gYear)))
g.add((emma, FOAF.interest, Literal("Cycling")))
g.add((emma, FOAF.interest, Literal("Music")))
g.add((emma, FOAF.interest, Literal("Travel")))
g.add((emma, EX.visited, Literal("Portugal")))
g.add((emma, EX.visited, Literal("Italy")))
g.add((emma, EX.visited, Literal("France")))
g.add((emma, EX.visited, Literal("Germany")))
g.add((emma, EX.visited, Literal("Denmark")))
g.add((emma, EX.visited, Literal("Sweden")))
g.add((emma, FOAF.age, Literal(36, datatype=XSD.integer)))

# Зв'язок між Кейдом та Еммою
g.add((cade, FOAF.knows, emma))
g.add((emma, FOAF.knows, cade))
g.add((cade, EX.metAt, Literal("Paris")))
g.add((cade, EX.metOn, Literal("2014-08", datatype=XSD.gYearMonth)))

# Збереження у файл TURTLE
g.serialize("output.ttl", format="turtle")

# Редагування: додати інформацію, що Кейд відвідував Німеччину
g.add((cade, EX.visited, Literal("Germany")))

# Виведення всіх трійок
print("All triples:")
for s, p, o in g:
    print(s, p, o)

# Виведення трійок, що стосуються лише Емми
print("\nTriples about Emma:")
for s, p, o in g.triples((emma, None, None)):
    print(s, p, o)

# Виведення трійок, що містять імена людей
print("\nTriples with names of people:")
for s, p, o in g.triples((None, FOAF.name, None)):
    print(s, p, o)
