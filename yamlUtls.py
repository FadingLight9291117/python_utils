import yaml
import logging

logging.basicConfig(level=logging.DEBUG)


def save2yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)


def yaml2dict(path):
    with open(path, encoding='utf-8') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    return d


if __name__ == '__main__':
    from jsonUtls import pretty_print_dict
    path = 'files/test.yaml'
    savepath = 'files/test_1.yaml'
    a = {'a': 1, 'b': [123, 123]}
    save2yaml(a, savepath)
    data = yaml2dict(path)
    pretty_print_dict(data)

    save2yaml(data, savepath)
