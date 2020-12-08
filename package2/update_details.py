def update_data2(voter_id, token, post_data, db, valid_info, list_data):
    # update_name = valid_info['update_user_name']
    # update_phone = valid_info['update_phone']
    # update_email = valid_info['update_email']
    # cur = db.cursor()
    # query = "SELECT * FROM register_table where id = ('" + str(voter_id) + "') OR token = ('" + str(token) + "')"
    # cur.execute(query)
    # table_data = cur.fetchall()
    # list_data = []
    # for data in table_data:
    #     dict_data = {"id": data[0], "user_name": data[1], "phone": data[2], "email": data[3],
    #                  "password": data[4], "token": data[5], "role_name": data[6]}
    #     list_data.append(dict_data)
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif voter_id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}
    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}

    elif post_data == valid_info:
        try:
            cur = db.cursor()
            query = "UPDATE register_table set user_name = ('" + str(update_name) + "'), " \
                                                                                    "phone = ('" + str(
                update_phone) + "'), email = ('" + str(update_email) + "') " \
                                                                       "WHERE id = ('" + str(
                voter_id) + "') AND token = ('" + str(token) + "')"
            cur.execute(query)
            db.commit()
        except:
            return {'Error': 'update_user_name or update_phone or update_email already exists'}
        return {'Data': 'successfully updated'}
    else:
        return {valid_info}

