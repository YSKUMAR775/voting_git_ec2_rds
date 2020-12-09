from uuid import uuid4


def reg_data(post_data, validations_data, encrypted_password, db):
    if post_data != validations_data:
        return validations_data
    else:
        user_name = post_data['user_name']
        phone = post_data['phone']
        email = post_data['email']
        admin = post_data['role_name']
        cur = db.cursor()
        try:
            query = "INSERT INTO register_table (id, user_name, phone, email, password, role_name) " \
                    "VALUES ('" + str(uuid4()) + "', '" + str(user_name) + "', '" + str(phone) + "', " \
                    "'" + str(email) + "', '" + str(encrypted_password) + "', '" + str(admin) + "')"
            cur.execute(query)
            db.commit()
        except Exception as e:
            return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace("'register_table.", "").replace("'", "").replace('\")', '')}

        return {"User": 'Registered successfully'}
