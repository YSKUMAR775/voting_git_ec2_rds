from werkzeug.security import generate_password_hash, check_password_hash


def pass2_encrypt2(post_data):
    new_password = post_data['new password']
    confirm_new_password = post_data['confirm new password']

    if new_password == confirm_new_password:
        encrypted_password = generate_password_hash(new_password, method="sha256")
        return encrypted_password
    else:
        return {'Error': "RE-Enter Password correctly"}


def pass2_check2(post_data, list_data):
    password = post_data['old password']

    if len(list_data) == 0:
        return {'Error': 'email not registered'}
    else:
        fetched_password = list_data[0]['password']
        password_check_final = check_password_hash(fetched_password, password)
        return password_check_final
