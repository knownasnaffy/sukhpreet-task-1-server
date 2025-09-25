from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    interests = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "salary": self.salary,
            "interests": self.interests,
        }


@app.before_request
def create_tables():
    db.create_all()


@app.route("/profile", methods=["GET", "POST", "PUT"])
def profile():
    if request.method == "GET":
        user = User.query.first()
        if user:
            return jsonify(
                {"status": 200, "message": "User found", "data": user.to_dict()}
            )
        else:
            return (
                jsonify({"status": 404, "message": "User not found", "data": None}),
                404,
            )

    if request.method == "POST":
        data = request.json
        user = User(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            salary=data["salary"],
            interests=data.get("interests", ""),
        )
        db.session.add(user)
        db.session.commit()
        return (
            jsonify({"status": 201, "message": "User added", "data": user.to_dict()}),
            201,
        )

    if request.method == "PUT":
        data = request.json
        user = User.query.first()
        if user:
            user.name = data.get("name", user.name)
            user.age = data.get("age", user.age)
            user.gender = data.get("gender", user.gender)
            user.salary = data.get("salary", user.salary)
            user.interests = data.get("interests", user.interests)
            db.session.commit()
            return jsonify(
                {"status": 200, "message": "User updated", "data": user.to_dict()}
            )
        else:
            return (
                jsonify({"status": 404, "message": "User not found", "data": None}),
                404,
            )


if __name__ == "__main__":
    app.run(debug=True)
