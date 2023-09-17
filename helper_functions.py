from country_cities import country_and_cities, seasons

def country_and_season_validation(country, season):
    error_message = []

    if country not in country_and_cities:
        error_message.append(
            "Error occurred in country or city name, Please select valid Country or City")
    if season not in seasons:
        error_message.append(f"Error occurred in season name, Please select season from {seasons}")

    return error_message
