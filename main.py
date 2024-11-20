from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse

import db_action
from db import create_db

app = Flask(__name__)
api = Api(app)


def row_to_json(shops: list):
    data = []
    for shop in shops:
        data.append({
            "id": shop.id,
            "author": shop.author,
            "text": shop.text
        })

    data_response = jsonify(data)
    data_response.status_code = 200
    return data_response


class ShopAPI(Resource):
    def get(self,id=0):
        if id:
            shop = db_action.get_shops(id)
            if shop:
                return row_to_json([shop])

            answer = jsonify("відсутній така інформація")
            answer.status_code = 400
            return answer

        shops = db_action.get_shops()
        return row_to_json(shops)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        id = db_action.add_shop(params.get("author"), params.get("text"))
        answer = jsonify(f"Нову інформацію додано під id{id}")
        return answer

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        answer = db_action.update_shop(id, params.get("author"), params.get("text"))
        answer = jsonify(answer)
        answer.status_code = 200
        return answer

    def delete(self, id):
        answer = db_action.delete_shop(id)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer


api.add_resource(ShopAPI, "/api/shops/", "/api/shops/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3000)