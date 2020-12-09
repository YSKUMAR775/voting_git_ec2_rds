def track_data(voter_id, token, db, list_data):
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif voter_id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}
    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}
    cur = db.cursor()
    query = "SELECT * FROM voting_table where voter_id = ('" + str(voter_id) + "')"
    cur.execute(query)
    fetch_candidates = cur.fetchall()
    list_data_polling = []
    for data in fetch_candidates:
        dict_data = {'candidate': data[0], 'voter_name': data[1], 'email': data[2],
                     'phone': data[3], 'voter_id': data[4]}
        list_data_polling.append(dict_data)

    query = "select * from register_table"
    cur.execute(query)
    table_data = cur.fetchall()
    count_table = {'total number of people': len(table_data)}

    query = "select * from voting_table"
    cur.execute(query)
    candidates_data = cur.fetchall()
    count_candidate = {'number of people voted': len(candidates_data)}

    if len(list_data_polling) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['id'] == list_data_polling[0]['voter_id']:
        return list_data_polling, count_table, count_candidate
    else:
        return {'Election': 'you are not voted'}
