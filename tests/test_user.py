import json

from app.model.user import User
from app.service.user import ns, user_list
from flask_restx import marshal

ENDPOINT = ns.path


def pretty_debug(o):
    from pprint import PrettyPrinter

    PrettyPrinter(width=200).pprint(o)


def test_user_get(client, database):
    test_user_obj = User(user_nm="abc")
    database.session.add(test_user_obj)
    database.session.commit()

    response = client.get(f"{ENDPOINT}/")
    pretty_debug(response.data)
    assert response.status_code == 200
    data = json.loads(response.data)

    assert len(data) == 1

    u_dict = marshal(data[0], user_list)
    u_obj = User(**u_dict)

    assert u_obj.user_nm == test_user_obj.user_nm
    assert u_obj.id == test_user_obj.id


def test_user_404(client):
    User.query.delete()
    response = client.get(f"{ENDPOINT}/")
    assert response.status_code == 404
    data = json.loads(response.data)
    assert list(data.keys()) == ["code", "message"]
