import json
import codecs


def load_data(filepath):
    if filepath:
        with codecs.open(filepath, 'r', 'utf8') as f:
            data = f.read()
    return data


def pretty_print_json(data):
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    data = load_data("datafile")
    pretty_print_json(data)
