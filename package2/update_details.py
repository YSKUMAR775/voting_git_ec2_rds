def update_data2(voter_id, token, post_data, db, valid_info, list_data):
    update_name = valid_info['update_user_name']
    update_phone = valid_info['update_phone']
    update_email = valid_info['update_email']

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
        except Exception as e:
            return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace("'register_table.", "").replace("'", "").replace('\")', '')}
        return {'Data': 'successfully updated'}
    else:
        return valid_info

