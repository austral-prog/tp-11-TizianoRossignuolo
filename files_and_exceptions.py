def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas_dict = {}

    try:
        with open(filename, 'r') as archivo:
            contenido = archivo.read()
            ventas = contenido.split(';')

            for venta in ventas:
                if venta != '':
                    partes = venta.split(':')
                    producto = partes[0].strip()
                    valor = float(partes[1].strip())

                    if producto in ventas_dict:
                        ventas_dict[producto].append(valor)
                    else:
                        ventas_dict[producto] = [valor]

    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no fue encontrado.")

    return ventas_dict


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, valores in data.items():
        total = sum(valores)
        promedio = total / len(valores)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
    pass
