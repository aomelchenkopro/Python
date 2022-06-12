def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&age=purple') == {'name': 'ferret', 'age': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&age=purple&') == {'name': 'ferret', 'age': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    parameters = {}
    name = query.find('name=')
    age = query.find('age=')
    semicolon = query.find(';')
    name = query[name + 5:semicolon if query.count(';') > 0 else len(query)] if name > -1 else None
    age = query[age + 4: query.find(';', semicolon + 1) if query.count(';') > 1 else len(query)] if age > -1 else None
    if name is not None:
        parameters['name'] = name.replace(';', '')
    if age is not None:
        parameters['age'] = age.replace(';', '')
    return parameters

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Sydney;age=33') == {'name': 'Sydney', 'age': '33'}
    assert parse_cookie('age=35') == {'age': '35'}
    assert parse_cookie('name=Taylor') == {'name': 'Taylor'}
    assert parse_cookie('name=Isabella=User;testage=22;test') == {'name': 'Isabella=User', 'age': '22'}
    assert parse_cookie('There are not any cookies') == {}
    assert parse_cookie('There are = not =; any cookies') == {}
    assert parse_cookie('There are = not name=Ashley; any cookies = ;') == {'name': 'Ashley'}
    assert parse_cookie('There are = not age=40') == {'age': '40'}
    assert parse_cookie('There is some name=Julia; cookies; =') == {'name': 'Julia'}
    assert parse_cookie('There is some name and age cookies; =') == {}