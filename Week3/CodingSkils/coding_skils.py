import json


def get_data_from_json(filename):
    with open(filename, 'r') as jf:
        data = json.load(jf)

        return data


data_dict_file = get_data_from_json('data.json')
print(data_dict_file)


def person_data(person_dict):
    name = '{} {}'.format(person_dict['first_name'], person_dict['last_name'])
    skills = [skills for skills in person_dict['skills']]
    lang_level = [(lang_dict['name'], lang_dict['level']) for lang_dict in skills]
    person_info = {name: lang_level}

    return person_info


def coding_skils_simply(data_dict):
    if not dict:
        return ''
    result = []
    for data in data_dict.values():
        for person_d in data:
            # print(person_d)
            person = person_data(person_d)
            result.append(person)
    return result


# data = coding_skils_simply(data_dict_file)


def coding_skils(simply_data):
    result = {}
    for person in simply_data:
        for key, values in person.items():
            for lang in values:
                lg = lang[0]
                level = lang[1]
                if lg not in result:
                    result[lg] = [key, level]
                elif lg in result and level > result[lg][1]:
                    result[lg] = [key, level]
    return result


# dict_to_str = coding_skils(data)

def print_result(end_dict):
    for key, value in end_dict.items():
        print('{} - {}'.format(key, value[0]))

# print_result(dict_to_str)
