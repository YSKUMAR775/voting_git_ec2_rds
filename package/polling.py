def poll_reg(voter_id, token, post_data, db):
    candidate = post_data['candidate_number']
    cur = db.cursor()

    nomi1 = 1
    nomi2 = 2
    nomi = ''
    if candidate == nomi1:
        nomi += 'Biden'
    elif candidate == nomi2:
        nomi += 'Trump'

    if candidate == 1 or candidate == 2:
        query = "SELECT * FROM register_table where id = ('" + str(voter_id) + "') OR token = ('" + str(token) + "')"
        cur.execute(query)
        fetch_data = cur.fetchall()
        list_data = []
        for data in fetch_data:
            dict_data = {'id': data[0], 'user_name': data[1], 'phone': data[2],
                         'email': data[3], 'password': data[4], 'token': data[5]}
            list_data.append(dict_data)

        if len(list_data) == 0:
            return {'Error': 'invalid voter_id and token'}
        elif voter_id != list_data[0]['id']:
            return {'Error': 'invalid voter_id'}
        elif token != list_data[0]['token']:
            return {'Error': 'invalid token'}

        try:
            query = "INSERT INTO voting_table values('" + str(nomi) + "', '" + str(list_data[0]['user_name']) + "' , " \
                    "'" + str(list_data[0]['email']) + "', '" + str(list_data[0]['phone']) + "', " \
                    "'" + str(voter_id) + "')"
            cur.execute(query)
            db.commit()
        except Exception as e:
            return {'Error': 'you have already voted'}
        return {'Elections': 'thank you for casting your vote'}

    else:
        return {'Error': 'please check the poll number'}
