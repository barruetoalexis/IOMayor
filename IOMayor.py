import re
import ctypes
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
                        io_costs.append(int(match.group(1)))
    except FileNotFoundError:
        show_alert("El archivo no se encontró.")
    except Exception as e:
        show_alert(f"Ocurrió un error: {e}")

    return io_costs

def get_max_io_cost(io_costs):
    if io_costs:
        io = max(io_costs)
        return io
    else:
        return None

def show_alert(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Alerta de Costo de I/O", 1)


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "io.txt")
io_costs = extract_io_cost(file_path)

if io_costs:
    io = get_max_io_cost(io_costs)
    if io is not None:
        show_alert(f"El mayor costo de I/O es: {io}")
else:
    show_alert("No se encontraron costos de I/O.")