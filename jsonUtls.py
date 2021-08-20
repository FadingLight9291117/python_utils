import json


def save2json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def json2dict(json_path):
    with open(json_path, encoding='utf-8') as f:
        d = json.load(f)
    return d


def pretty_print_dict(data):
    data = json.dumps(data, indent=4, ensure_ascii=False,
                      sort_keys=False, separators=(',', ': '))
    print(data)


if __name__ == '__main__':
    filename = './files/test.json'
    jsondata = json2dict(filename)
    pretty_print_dict(jsondata)
