import yaml


def save2yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)


def yaml2dict(path):
    with open(path, encoding='utf-8') as f:
        d = yaml.load(f)
    return d


if __name__ == '__main__':
    from jsonUtls import pretty_print_dict
    path = 'files/test.yaml'
    savepath = 'files/test_1.yaml'
    data = yaml2dict(path)
    pretty_print_dict(data)

    save2yaml(data, savepath)