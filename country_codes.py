from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    ''' according to the country name, get the counry code '''
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    # if can't find the country
    return None
'''
# test
print(get_country_code('Andorra'))
print(get_country_code('China'))
'''