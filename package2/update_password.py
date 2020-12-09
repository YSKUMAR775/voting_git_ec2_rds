def update_password(voter_id, token, valid_password, post_data, db, password_check_final, encrypted_password, list_data):

    new_password = post_data['new password']
    confirm_new_password = post_data['confirm new password']

    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif voter_id != list_data[0]['id']:
        return {'Error': 'invalid voter_id'}
    elif token != list_data[0]['token']:
        return {'Error': 'invalid token'}

    if valid_password == post_data:
        if password_check_final == bool(1):
            if new_password == confirm_new_password:
                cur = db.cursor()
                query = " UPDATE register_table SET password = ('" + str(encrypted_password) + "') WHERE id = ('" + str(
                    voter_id) + "')"
                cur.execute(query)
                db.commit()
                return {'password': 'updated successfully'}
            else:
                return encrypted_password
        else:
            return {"Error": "incorrect password"}
    else:
        return valid_password

