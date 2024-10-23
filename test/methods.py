from test.data import TEST_DATA


class AllMethod:
    @staticmethod
    def extract_test_data(key):
        """Extract data for test by key"""
        try:
            data = TEST_DATA[key]
            return tuple(data.values())
        except KeyError as e:
            raise ValueError(f"Missing key in test data: {e}")

    @staticmethod
    def check_response(response, status_code):
        """Check expected status code in response"""
        try:
            assert response.status_code == status_code, f"Unexpected status code: {response.status_code}. Response: {response.text}"
        except KeyError as e:
            raise ValueError(f"Missing key in test data: {e}")
