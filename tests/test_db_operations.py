from src.database.operations import select


def test_database_operation_select(mocker):
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "accurate",
        "db": "test_db",
    }

    mock_responce = [
        {"item_id": 1, "price": 20, "name": "item 1"},
        {"item_id": 2, "price": 30, "name": "item 2"},
        {"item_id": 3, "price": 40, "name": "item 3"},
    ]
    mock_object = mocker.patch(
        "src.database.operations.create_db_response", return_value=mock_responce
    )

    sql = "select * from items"
    db_result = select(db_config=db_config, sql=sql)

    assert len(db_result) > 0

    item_keys = db_result[0].keys()

    assert "item_id" in item_keys
    assert "price" in item_keys
    assert "name" in item_keys
    assert mock_object.call_count == 1
    assert mock_object.call_args_list[0][0][0] == db_config
    assert mock_object.call_args_list[0][0][1] == sql
