import json


def person_data(data_dict):
    result = {}
    for people in data_dict.values():
        for line in people:
            full_name = '{} {}'.format(line['first_name'], line['last_name'])
            for skill in line['skills']:
                if skill['name'] not in result:
                    result[skill['name']] = [full_name, skill['level']]
                elif skill['name'] in result and skill['level'] > result[skill['name']][1]:
                    result.update({skill['name']: [full_name, skill['level']]})
            #     print(skill)
            # print(line)
    return result


def json_to_dict(filename):
    with open(filename, 'r') as f:
        content = json.load(f)

    return content

#
# data_dict = json_to_dict('data.json')
# # print(data_dict)
# print(person_data(data_dict))
