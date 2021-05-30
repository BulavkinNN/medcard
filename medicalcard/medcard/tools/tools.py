import random


def get_random_analysis(name="", laboratory="", ):
    INDICATORS_LIST = ['WBC', 'LYM', 'MON', 'NEU', 'EOS', 'BAS', 'RBC', 'HGB', 'MCV', 'MCHC', 'PLT', 'MPV']
    result = {key: random.randint(0, 100) for key in INDICATORS_LIST}
    return {
        'name': name,
        'laboratory': laboratory,
        'result': result
    }
