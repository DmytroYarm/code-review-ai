from test.data import TEST_DATA


class AllMethod:
    @staticmethod
    def extract_test_data(key):
        """Извлекает данные для теста по ключу, возвращает кортеж всех значений."""
        try:
            data = TEST_DATA[key]
            return tuple(data.values())
        except KeyError as e:
            raise ValueError(f"Missing key in test data: {e}")

    @staticmethod
    def check_response(response):
        """Извлекает данные для теста по ключу, возвращает кортеж всех значений."""
        try:
            assert response.status_code == 200
        except KeyError as e:
            raise ValueError(f"Missing key in test data: {e}")
