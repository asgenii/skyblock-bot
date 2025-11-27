def main(_path):
    import json

    with open(_path, 'r', encoding='utf-8') as file:
        return json.load(file)