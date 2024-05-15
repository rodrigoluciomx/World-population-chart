# Cualquier archivo creado en python, es un modulo.
def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_country(data, country):
    result = list(
        filter(lambda item: item['Country/Territory'] == country, data))
    return result


def get_WorldPopulationPercentage(data):
    percentages = list(
        map(lambda item: item['World Population Percentage'], data))
    return percentages


def get_CountriesNames(data):
    countries = list(map(lambda item: item['Country/Territory'], data))
    return countries


# Mi version de population_by_country
def get_population_data(country, dataset):
    new_list = []
    for dict in dataset:
        if dict['Country/Territory'] == country:
            new_list = [
                dict['2022 Population'], dict['2020 Population'],
                dict['2015 Population'], dict['2010 Population'],
                dict['2000 Population'], dict['1990 Population'],
                dict['1980 Population'], dict['1970 Population']
            ]
    return new_list
