def read_list_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def write_list_to_file(file_path, list_data):
    with open(file_path, 'w') as file:
        for item in list_data:
            file.write(f"{item}\n")

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def process_sizes(sizes):
    numeric_sizes = [size for size in sizes if is_numeric(size)]
    return ','.join(sorted(set(numeric_sizes), key=lambda x: float(x)))

def process_skus(list_skus):
    sku_dict = {}
    for sku in list_skus:
        if ':' in sku:
            base_sku, sizes = sku.split(':')
            sizes = sizes.split(',')
        else:
            base_sku, sizes = sku, []

        if base_sku in sku_dict:
            sku_dict[base_sku].update(sizes)
        else:
            sku_dict[base_sku] = set(sizes)

    return [f"{sku}:{process_sizes(sizes)}" if sizes else sku for sku, sizes in sku_dict.items()]

def combine_and_process_lists(list1, list2):
    combined_list = list1 + list2
    return process_skus(combined_list)

# Replace these paths with your actual file paths
file_path1 = r'C:\Users\Tristan\Desktop\valor.txt'
file_path2 = r'C:\Users\Tristan\Desktop\valor2.txt'
output_file_path = r'C:\Users\Tristan\Desktop\combined_list.txt'  # Path for the output file

list1 = read_list_from_file(file_path1)
list2 = read_list_from_file(file_path2)

processed_list = combine_and_process_lists(list1, list2)

write_list_to_file(output_file_path, processed_list)
print(f"Combined list written to {output_file_path}")
