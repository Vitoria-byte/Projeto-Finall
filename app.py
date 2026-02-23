from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db

app = Flask(__name__)
CORS(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    db = get_db()
    cursor = db.cursor(dictionary=True)

    sql = "SELECT * FROM users WHERE email=%s AND senha=%s"
    cursor.execute(sql, (data["email"], data["senha"]))
    user = cursor.fetchone()

    if user:
        return jsonify(user)
    return jsonify({"erro":"Login inválido"}), 401

@app.route("/recursos")
def listar():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM recursos")
    return jsonify(cursor.fetchall())

@app.route("/recursos", methods=["POST"])
def cadastrar():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    sql = "INSERT INTO recursos (nome,tipo,status) VALUES (%s,%s,%s)"
    cursor.execute(sql, (data["nome"], data["tipo"], data["status"]))
    db.commit()

    return jsonify({"msg":"cadastrado"})

@app.route("/recursos/<int:id>", methods=["DELETE"])
def deletar(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM recursos WHERE id=%s", (id,))
    db.commit()
    return jsonify({"msg":"deletado"})

@app.route("/dashboard")
def dashboard():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM recursos")
    total_recursos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    return jsonify({
        "recursos": total_recursos,
        "usuarios": total_users
    })

app.run(debug=True)
