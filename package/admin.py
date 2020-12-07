def track_data(poll, voter_id, token, db):
    candidate1 = 1
    candidate2 = 2

    if poll == candidate1:
        poll = 'Biden'
    elif poll == candidate2:
        poll = 'Trump'
    elif candidate1 != poll or candidate2 != poll:
        return {'Error': 'please enter valid poll_number'}

    cur = db.cursor()
    query = "SELECT * FROM register_table where id = ('" + str(voter_id) + "') OR token = ('" + str(token) + "')"
    cur.execute(query)
    fetch_data = cur.fetchall()

    list_data = []
    for data in fetch_data:
        dict_data = {'id': data[0], 'user_name': data[1], 'phone': data[2],
                     'email': data[3], 'password': data[4], 'token': data[5], "role_name": data[6]}
        list_data.append(dict_data)

    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}

    elif voter_id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}

    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}

    elif list_data[0]['role_name'] == "admin":
        query = "select * from voting_table where candidate = ('" + str(poll) + "')"
        cur.execute(query)
        fetch_data = cur.fetchall()
        print(fetch_data)
        return {'Total number of votes for ' + poll: len(fetch_data)}

    else:
        return {'Error': 'You are not an admin'}
