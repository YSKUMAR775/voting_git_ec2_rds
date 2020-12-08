def update_data2(voter_id, token, post_data, db, valid_info):
    update_name = valid_info['update_user_name']
    update_phone = valid_info['update_phone']
    update_email = valid_info['update_email']
    if post_data == valid_info:
        try:
            cur = db.cursor()
            query = "UPDATE register_table set user_name = ('" + str(update_name) + "'), " \
                    "phone = ('" + str(update_phone) + "'), email = ('" + str(update_email) + "') " \
                    "WHERE id = ('" + str(voter_id) + "') OR token = ('" + str(token) + "')"
            cur.execute(query)
            db.commit()
        except:
            return{'Error': 'update_user_name or update_phone or update_email already exists'}
        return {'Data': 'successfully updated'}
    else:
        return {valid_info}
