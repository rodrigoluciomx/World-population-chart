import utils  #Llamando al archivo mod.py que está dentro de la misma carpeta
import read_csv
import charts

def display_WorldPopulationPercentage(data):
    percentages = list(
        map(lambda value: float(value),
            utils.get_WorldPopulationPercentage(data)))
    #Obteniendo los nombres de todos los paises
    labels = utils.get_CountriesNames(data)
    charts.generate_pie_chart(labels, percentages)
    pass

def run():
    data = read_csv.read_csv('./data.csv')
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(
            country)  #Usando las funciones dentro del archivo
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

    display_WorldPopulationPercentage(data)

#Control de dualidad
#Podemos usar el main como un modulo sin que se ejecute por si solo
#Podemos ejecutar el script desde la terminal
if __name__ == '__main__':
    run()
