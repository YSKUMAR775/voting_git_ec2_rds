def nomination_data(id, token, db):
    cur = db.cursor()
    query = " select * from register_table where id = ('" + str(id) + "') OR token = %s"
    cur.execute(query, token)
    fetch_data = cur.fetchall()
    list_data = []
    for data in fetch_data:
        dict_data = {"id": data[0], "user_name": data[1], "phone": data[2],
                     "email": data[3], "password": data[4], "token": data[5]}

        list_data.append(dict_data)
    if len(list_data) == 0:
        return {'Error': "invalid voter_id and token"}
    elif id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}
    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}
    else:
        return "Hello " + list_data[0]["user_name"] + ', you can vote for the candidate by passing a value which has ' \
                                                   'given below:', {'Biden': 1, 'Trump': 2}
