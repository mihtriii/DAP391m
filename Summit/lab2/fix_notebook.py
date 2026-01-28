import json

file_path = '/Users/mihtriii/Documents/GitHub/DAP391m/Summit/lab2/RandomForests.ipynb'

try:
    with open(file_path, 'r') as f:
        data = json.load(f)

    target_cell = None
    for cell in data['cells']:
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            # Convert list to string to search or search in list
            if "import pydoc\n" in source:
                target_cell = cell
                break

    if target_cell:
        new_source = [
            "import pydot\n",
            "from sklearn.tree import export_graphviz\n",
            "\n",
            "tree = rf.estimators_[0]\n",
            "export_graphviz(tree, out_file=\"tree.dot\", feature_names=features_list, rounded=True, precision=1)\n",
            "\n",
            "(graph, ) = pydot.graph_from_dot_file(\"tree.dot\")\n",
            "graph.write_png(\"tree.png\")\n"
        ]
        target_cell['source'] = new_source
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=1)
        
        print("Fixed notebook.")
    else:
        print("Target cell not found.")

except Exception as e:
    print(f"Error: {e}")
