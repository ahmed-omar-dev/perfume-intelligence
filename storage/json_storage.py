import json


class JSONStorage:
    def __init__(self, file_path):
        self.file_path = file_path


    def save(self, data):
        with open(
            self.file_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4,
            )


    def load(self):
        try:
            with open(
                self.file_path,
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            return data

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []