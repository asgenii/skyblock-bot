def main(_path):
    import yaml

    with open(_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)