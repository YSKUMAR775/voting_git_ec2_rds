def acct_lgn2(token, voter_id, db):
    cur = db.cursor()
    query = "SELECT * FROM register_table where id = ('" + str(voter_id) + "') OR token = ('" + str(token) + "')"
    cur.execute(query)
    fetch_data = cur.fetchall()
    list_data = []
    for data in fetch_data:
        dict_data = {'id': data[0], 'user_name': data[1], 'phone': data[2],
                     'email': data[3], 'password': data[4], 'token': data[5], "role_name": data[6]}
        list_data.append(dict_data)
    return list_data
