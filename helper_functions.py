from country_cities import country_and_cities, seasons


def is_country_present(country):
    if country in country_and_cities:
        return country is not None


def is_season_present(season):
    if season in seasons:
        return season is not None
