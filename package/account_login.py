def auth_lgn(post_data, db):
    email_check = post_data["email"]
    # password_check = data["password"]

    cur = db.cursor()
    query = "select * from register_table where email = ('" + str(email_check) + "') "
    cur.execute(query)
    fetch_data = cur.fetchall()
    list_data = []
    for data in fetch_data:
        dict_data = {"id": data[0], "user_name": data[1], "phone": data[2], "email": data[3], "password": data[4]}
        list_data.append(dict_data)

    return list_data
