from flask import Flask, request, jsonify
from package_data import password_encryption, validations, account_register, database, \
    account_login, login_token, nomination_candidates, polling, tracking, admin

app = Flask(__name__)


@app.route("/register", methods=['POST'])
def register():
    post_data = request.get_json()
    encrypted_password = password_encryption.pass_encrypt(post_data)
    validations_data = validations.valid(post_data)
    db = database.db_connect()
    registered_data = account_register.reg_data(post_data, validations_data, encrypted_password, db)

    return jsonify(registered_data)


@app.route("/login", methods=["POST"])
def login_data():
    post_data = request.get_json()
    db = database.db_connect()
    list_data = account_login.auth_lgn(post_data, db)
    password_check_final = password_encryption.pass_check(post_data, list_data)
    token_generate = login_token.lgn_token(list_data, post_data, db, password_check_final)

    return jsonify(token_generate)


@app.route("/vote/voter_id=<id>", methods=['GET'])
def check_data(id):
    token = request.headers['token_data']
    db = database.db_connect()
    registered_data = nomination_candidates.nomination_data(id, token, db)

    return jsonify(registered_data)


@app.route("/vote/data/voter_id=<voter_id>", methods=['POST'])
def polling_register(voter_id):
    token = request.headers['token_data']
    post_data = request.get_json()
    db = database.db_connect()
    voting_register = polling.poll_reg(voter_id, token, post_data, db)

    return jsonify(voting_register)


@app.route("/vote/data/voter_id=<voter_id>", methods=['GET'])
def tracking_votes(voter_id):
    token = request.headers['token_data']
    db = database.db_connect()
    track_votes = tracking.track_data(voter_id, token, db)

    return jsonify(track_votes)


@app.route("/vote/data/voter_id=<voter_id>/poll_number=<int:poll>", methods=['GET'])
def admin_login(voter_id, poll):
    token = request.headers['token_data']
    db = database.db_connect()
    admin_check = admin.track_data(poll, voter_id, token, db)

    return jsonify(admin_check)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
