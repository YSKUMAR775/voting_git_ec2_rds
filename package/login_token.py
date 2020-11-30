import jwt
import datetime

JWT_SECRET_KEY = 'this is the secret key'


def lgn_token(list_data, post_data, db, password_check_final):
    if len(list_data) == 0:
        return {'Error': 'email not registered'}

    email_check = post_data["email"]
    password_check = post_data["password"]
    if password_check_final is not bool(1):
        return {'Error': 'Invalid Password !!'}
    
    elif email_check == list_data[0]["email"]:
        token = jwt.encode(
            {'email': email_check, 'password': password_check,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, JWT_SECRET_KEY)

        token_data = token.decode('UTF-8')

        cur = db.cursor()
        try:
            query = "update voting_table set token = ('" + str(token_data) + "') where  email = ('" + str(email_check) + "')"
            cur.execute(query)
            db.commit()
        except Exception as err:
            return {'Error': 'InterfaceError'}

        return {"id": list_data[0]["id"], "Token": token_data}
    else:
        return {'Error': 'Invalid Password !!'}
