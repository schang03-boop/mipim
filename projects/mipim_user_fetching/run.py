from algoliasearch.search_client import SearchClient

_API_KEY = 'ZjIyZTIzZDZiMzE4ZTUxMWFiOTk0NzdmZGY0NmNiM2QyMmIyYmE4Nzg1ZTEwODNhOGJhMmFkZGQ0ODkxNDc5ZXJlc3RyaWN0SW5kaWNlcz1ldmUtMzJmODIwZmMtNTg5OS00MTk0LWFjMjUtMWU0ODUzMzZkYTgzXyomdmFsaWRVbnRpbD0xNjc3NTk0NDM4'


def run():
    client = SearchClient.create("8CD2G7QY2D", api_key=_API_KEY)
    index = client.init_index('eve-32f820fc-5899-4194-ac25-1e485336da83_en-gb')

    #res = index.search('query string')

    return


if __name__ == '__main__':
    print(run())