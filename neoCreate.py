from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="*Joaquim2016")

# Create some nodes with labels

user = db.labels.create("Usuário")
u1 = db.nodes.create(name="Bob")
u2 = db.nodes.create(name="Alice")
u3 = db.nodes.create(nome="Lea")
u4 = db.nodes.create(nome="Ana")
u5 = db.nodes.create(nome="Joel")

user.add(u1, u2, u3, u4, u5)

u1.relationships.create('follows', u2)
u4.relationships.create('follows', u1)
u2.relationships.create('follows', u3)
u2.relationships.create('follows', u5)