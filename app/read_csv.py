import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(
            reader
        )  #obteniendo la primera fila, la fila que tiene los nombres de las columnas
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {
                key: value
                for key, value in iterable
            }  #transformandolo a un diccionario
            data.append(country_dict)
        return data


def get_header(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        return header


if __name__ == '__main__':
    dataset = read_csv('./app/data.csv')
    print(get_population_data(input('Escribe el nombre de un pais\n'),
                              dataset))
