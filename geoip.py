MOCK_DB = {'127.0.0.1': {'country': 'Localhost', 'city': 'Local'}}
def lookup(ip: str) -> dict:
    return MOCK_DB.get(ip, {'country': 'Indonesia', 'city': 'Jakarta'})
