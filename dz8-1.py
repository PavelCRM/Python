import os
import json
import csv
import pickle

def traverse_directory(directory):
    results = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        dir_size = 0

        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            results.append({
                'name': file,
                'type': 'file',
                'parent_directory': root,
                'size': size
            })
            dir_size += size
            total_size += size

        results.append({
            'name': os.path.basename(root),
            'type': 'directory',
            'parent_directory': os.path.dirname(root),
            'size': dir_size
        })

    results.append({
        'name': os.path.basename(directory),
        'type': 'directory',
        'parent_directory': None,
        'size': total_size
    })

    # Save results to JSON
    with open('directory_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Save results to CSV
    with open('directory_results.csv', 'w', newline='') as csv_file:
        fieldnames = ['name', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Save results to Pickle
    with open('directory_results.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

# Пример вызова функции
traverse_directory('/path/to/directory')

