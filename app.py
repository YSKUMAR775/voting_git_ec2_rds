from flask import Flask, request, jsonify
from package import password_encryption, validations, account_register, database, account_login, login_token, \
    nomination_candidates, polling, tracking, admin
from package2 import update_password, account_login2, password_encryption2, validations2, update_details, database2

app = Flask(__name__)


@app.route("/register", methods=['POST'])
def register():
    db = database.db_connect()
    post_data = request.get_json()
    encrypted_password = password_encryption.pass_encrypt(post_data)
    validations_data = validations.valid(post_data)
    registered_data = account_register.reg_data(post_data, validations_data, encrypted_password, db)

    return jsonify(registered_data)


@app.route("/login", methods=["POST"])
def login_data():
    db = database.db_connect()
    post_data = request.get_json()
    list_data = account_login.auth_lgn(post_data, db)
    password_check_final = password_encryption.pass_check(post_data, list_data)
    token_generate = login_token.lgn_token(list_data, post_data, db, password_check_final)

    return jsonify(token_generate)


@app.route("/data/voter_id=<id>", methods=['GET'])
def check_data(id):
    db = database.db_connect()
    token = request.headers['token_data']
    registered_data = nomination_candidates.nomination_data(id, token, db)

    return jsonify(registered_data)


@app.route("/data/vote/voter_id=<voter_id>", methods=['POST'])
def polling_register(voter_id):
    db = database.db_connect()
    token = request.headers['token_data']
    post_data = request.get_json()
    voting_register = polling.poll_reg(voter_id, token, post_data, db)
    return jsonify(voting_register)


@app.route("/data/vote/voter_id=<voter_id>", methods=['GET'])
def tracking_votes(voter_id):
    db = database.db_connect()
    token = request.headers['token_data']
    track_votes = tracking.track_data(voter_id, token, db)

    return jsonify(track_votes)


@app.route("/data/vote/voter_id=<voter_id>/poll_number=<int:poll>", methods=['GET'])
def admin_login(voter_id, poll):
    db = database.db_connect()
    token = request.headers['token_data']
    admin_check = admin.track_data(poll, voter_id, token, db)

    return jsonify(admin_check)


@app.route("/data/password/voter_id=<voter_id>", methods=['POST'])
def update_passwd(voter_id):
    my_db = database2.db_conn()
    post_data = request.get_json()
    token = request.headers['token_data']
    list_data = account_login2.acct_lgn2(voter_id, token, my_db)
    password_check_final = password_encryption2.pass2_check2(post_data, list_data)
    encrypted_password = password_encryption2.pass2_encrypt2(post_data)
    valid_password = validations2.valid2(post_data)
    change_password = update_password.update_password(voter_id, valid_password, post_data, my_db, password_check_final, encrypted_password)

    return jsonify(change_password)


@app.route("/data/update/voter_id=<voter_id>", methods=['POST'])
def update_detail(voter_id):
    my_db = database2.db_conn()
    post_data = request.get_json()
    token = request.headers['token_data']
    valid_info = validations2.valid3(post_data)
    update_info = update_details.update_data2(voter_id, token, post_data, my_db, valid_info)

    return jsonify(update_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
