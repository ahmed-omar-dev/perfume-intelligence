from storage.json_storage import JSONStorage


# Tests saving and loading JSON data.
def test_save_and_load(tmp_path):
    file_path = (
        tmp_path / "test_perfumes.json"
    )

    storage = JSONStorage(
        file_path
    )

    data = [
        {
            "perfume_id": "P001",
            "name": "Test Perfume",
        }
    ]

    storage.save(data)

    result = storage.load()

    assert result == data


# Tests loading when the file does not exist.
def test_load_missing_file(tmp_path):
    file_path = (
        tmp_path / "missing.json"
    )

    storage = JSONStorage(
        file_path
    )

    result = storage.load()

    assert result == []


# Tests loading an empty JSON file.
def test_load_empty_file(tmp_path):
    file_path = (
        tmp_path / "empty.json"
    )

    file_path.write_text(
        "",
        encoding="utf-8",
    )

    storage = JSONStorage(
        file_path
    )

    result = storage.load()

    assert result == []