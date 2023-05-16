'''
Creational pattern
- builder pattern
'''


class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, columns):
        self.query += f"SELECT {','.join(columns)} "
        return self

    def from_table(self, table):
        self.query += f"FROM {table} "
        return self

    def where(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def limit(self, limit):
        self.query += f"LIMIT {limit} "
        return self

    def build(self):
        return self.query

    # Usage


query_builder = QueryBuilder().select(['name', 'age']).from_table(
    'users').where('age > 18').limit(10)
query = query_builder.build()

print(query)
