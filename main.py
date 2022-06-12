# Function searches parameters
def parse(query: str) -> dict:
    parameters = {}
    if query.find('?'):
        name = query.find('name=')
        color = query.find('color=')
        ampersand = query.find('&')
        name = query[name + 5:ampersand if query.count('&') > 0 else len(query)] if name > -1 else None
        color = query[color + 6: query.find('&', ampersand + 1) if query.count('&') > 1 else len(query)] if color > -1 else None
        if name is not None:
            parameters['name'] = name.replace('&', '')
        if color is not None:
            parameters['color'] = color.replace('&', '')
    return parameters


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?color=Yellow') == {'color': 'Yellow'}
    assert parse('http://example.com/?color=Gray&') == {'color': 'Gray'}
    assert parse('http://example.com/?name=Emilу&') == {'name': 'Emilу'}
    assert parse('http://name.com/') == {}
    assert parse('http://color.com/') == {}
    assert parse('http://color.com/?') == {}
    assert parse('http://color.com/?&=') == {}
    assert parse('https://example.com/path/to/page?name=Ella&color=red&test') == {'name': 'Ella', 'color': 'red'}
    assert parse('https://example.com/path/to/page?name=Ella&testcolor=red&test') == {'name': 'Ella', 'color': 'red'}
    assert parse('https://example.com/path/to/page?name=Ella&test') == {'name': 'Ella'}

def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

