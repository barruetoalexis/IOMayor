import re
import os

def extract_io_cost(file_path):
    io_costs = []
    phrase = "Total actual I/O cost for this command:"

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if phrase in line:
                    match = re.search(rf"{phrase}\s*([0-9]+(?:\.[0-9]+)?)", line)
                    if match:
                        io_costs.append(float(match.group(1)))
    except FileNotFoundError:
        save_to_file(file_path, "El archivo no se encontró.")
    except Exception as e:
        save_to_file(file_path, f"Ocurrió un error: {e}")

    return io_costs

def get_max_io_cost(io_costs):
    if io_costs:
        IOMayor = int(max(io_costs))
        return IOMayor
    else:
        return None

def save_to_file(file_path, message):
    output_file_path = os.path.splitext(file_path)[0] + "_resultado.txt"
    with open(output_file_path, 'w') as file:
        file.write(message)


script_dir = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(script_dir):
    if filename.endswith(".txt") and not filename.endswith("_resultado.txt"):
        file_path = os.path.join(script_dir, filename)
        filename_without_ext = os.path.splitext(filename)[0]
        
        io_costs = extract_io_cost(file_path)
        
        if io_costs:
            IOMayor = get_max_io_cost(io_costs)
            if IOMayor is not None:
                save_to_file(file_path, f"El mayor costo de I/O en el SP '{filename_without_ext}' es: {IOMayor}")

