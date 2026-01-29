import json

file_path = '/Users/mihtriii/Documents/GitHub/DAP391m/Summit/lab3/boosting.ipynb'

try:
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Find the cell with the StratifiedKFold error
    for cell in data['cells']:
        if cell.get('cell_type') == 'code':
            source = "".join(cell.get('source', []))
            if "StratifiedKFold(n_splits=10, random_state=7)" in source:
                new_source = []
                for line in cell['source']:
                    if "StratifiedKFold(n_splits=10, random_state=7)" in line:
                         new_source.append(line.replace("StratifiedKFold(n_splits=10, random_state=7)", "StratifiedKFold(n_splits=10, shuffle=True, random_state=7)"))
                    else:
                        new_source.append(line)
                cell['source'] = new_source
                print("Fixed StratifiedKFold initialization.")
                break

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=1)

except Exception as e:
    print(f"Error: {e}")
