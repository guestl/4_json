import json
import codecs
import sys
import os.path


def load_data(filepath):
    if filepath:
        with codecs.open(filepath, 'r', 'utf8') as f:
            json_file_data = f.read()
    return json_file_data


def pretty_print_json(json_data):
    parsed_json_data = json.loads(json_data)
    print(json.dumps(parsed_json_data,
          indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You have to use json file name as parameters. \
               \nExample: python pprint_json.py <path to json file>")
        exit()

    json_filename = sys.argv[1]

    if os.path.isfile(json_filename):
        readed_data = load_data(json_filename)
        pretty_print_json(readed_data)
    else:
        print("Json file '%s' must exists" % json_filename)
