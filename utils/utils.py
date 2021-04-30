def convert_lead_into_prospect(person_id, internal_qualification_result):
    print('-' * 50)
    print(f'person id: {person_id}, qualification result: {internal_qualification_result}')
    if internal_qualification_result > 60:
        print('Converted into prospect')
    print('-' * 50)