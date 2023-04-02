# Bernhards Arnitis 221RDB128 11.grupa
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.skaitlis = int(query[1])
        if self.type == 'add':
            self.vards = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.skaitlis] = cur_query.vards
      #  elif cur_query.type == 'find':

        elif cur_query.type == 'del':
            if cur_query.skaitlis in contacts:
                del contacts[cur_query.skaitlis]
        else:
            response = contacts.get(cur_query.skaitlis, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
