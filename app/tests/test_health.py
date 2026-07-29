def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    body = response.get_json()

    assert body["status"] == "healthy"


def test_version(client):
    response = client.get("/version")

    assert response.status_code == 200