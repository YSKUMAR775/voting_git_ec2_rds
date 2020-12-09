def track_data(poll, voter_id, token, db, list_data):
    candidate1 = 1
    candidate2 = 2

    if poll == candidate1:
        poll = 'Biden'
    elif poll == candidate2:
        poll = 'Trump'
    elif candidate1 != poll or candidate2 != poll:
        return {'Error': 'please enter valid poll_number'}

    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}

    elif voter_id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}

    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}

    elif list_data[0]['role_name'] == "admin":
        cur = db.cursor()
        query = "select * from voting_table where candidate = ('" + str(poll) + "')"
        cur.execute(query)
        fetch_data = cur.fetchall()
        print(fetch_data)
        return {'Total number of votes for ' + poll: len(fetch_data)}

    else:
        return {'Error': 'You are not an admin'}
