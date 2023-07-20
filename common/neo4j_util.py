from py2neo import Graph


# neo4j_url = "bolt://localhost:7687"
# neo4j_auth = ("neo4j", "ysh121726")


def connect_neo4j():
    # neo4j = Graph(neo4j_url, neo4j_auth)
    neo4j = Graph('http://localhost:7474', username="neo4j", password="ysh121726")
    return neo4j


class Neo4jQuery:
    def __init__(self):
        self.graph = connect_neo4j()

    def run(self, cql):
        result = []
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result
