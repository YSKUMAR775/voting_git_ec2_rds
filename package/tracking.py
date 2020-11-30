def track_data(voter_id, token, db):
    cur = db.cursor()
    query = "SELECT * FROM voting_table where id = ('" + str(voter_id) + "') OR token = ('" + str(token) + "')"
    cur.execute(query)
    table_data = cur.fetchall()
    list_data_voter = []
    for data in table_data:
        dict_data = {"id": data[0], "user_name": data[1], "phone": data[2], "email": data[3],
                     "password": data[4], "token": data[5], "role_name": data[6]}
        list_data_voter.append(dict_data)

    if len(list_data_voter) == 0:
        return {'Error': 'invalid voter_id or token'}
    elif voter_id != list_data_voter[0]['id']:
        return {'Error': 'invalid voter_id'}
    elif token != list_data_voter[0]['token']:
        return {'Error': 'invalid token'}

    query = "SELECT * FROM voting_candidates where voter_id = ('" + str(voter_id) + "')"
    cur.execute(query)
    fetch_candidates = cur.fetchall()
    list_data_polling = []
    for data in fetch_candidates:
        dict_data = {'id': data[0], 'candidate': data[1], 'voter_name': data[2],
                     'email': data[3], 'phone': data[4], 'voter_id': data[5], 'token': data[6]}
        list_data_polling.append(dict_data)

    query = "select * from voting_table"
    cur.execute(query)
    table_data = cur.fetchall()
    count_table = {'total number of people': len(table_data)}

    query = "select * from voting_candidates"
    cur.execute(query)
    candidates_data = cur.fetchall()
    count_candidate = {'number of people voted': len(candidates_data)}

    if len(list_data_polling) == 0:
        return {'Error': 'invalid voter_id or token'}
    elif list_data_voter[0]['id'] == list_data_polling[0]['voter_id']:
        return list_data_polling, count_table, count_candidate
    else:
        return {'Election': 'you are not voted'}
