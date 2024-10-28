def create_json_file(filename, data):
    import json
    with open(f'./data/{filename}', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent=4)