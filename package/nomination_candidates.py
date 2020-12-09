def nomination_data(voter_id, token, list_data):
    if len(list_data) == 0:
        return {'Error': "invalid voter_id and token"}
    elif voter_id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}
    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}
    else:
        return "Hello " + list_data[0]["user_name"] + ', you can vote for the candidate by passing a value which has ' \
                                                   'given below:', {'Biden': 1, 'Trump': 2}
