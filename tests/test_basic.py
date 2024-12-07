# Обязательно с test_*_ в начале имени файла
def test_index_page(client):
    responce = client.get("/")
    assert responce.status_code == 200
    assert "Hello world" in responce.text
