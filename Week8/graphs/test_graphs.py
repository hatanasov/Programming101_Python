import unittest
import graphs


class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.data = {
            "a": 10,
            "b": "somestring",
            "c": {
                "D": {
                    "d": [True, False]
                },
                "e": (
                    {
                        "f": True,
                        "g": [1, 2, 3]
                    },
                )
            },
            "h": [[[[{"z": "Z"}]]]]
        }
        self.d = {'e': [{'f': True, 'g': [1, 2, 3]}]}
        self.data_all = {
            "a": 10,
            "b": {"a": 20},
            "c": [
                {"b": [{"a": 30}]}
            ]
        }

    def test_deep_find_simple_data(self):
        key = "a"
        self.assertEqual(graphs.deep_find(self.data, key), self.data[key])

    def test_deep_find_value_is_dict(self):
        key = "d"
        result = [True, False]
        self.assertEqual(graphs.deep_find(self.data, key), result)

    def test_deep_find_of_iterable_value(self):
        key = "g"
        result = [1, 2, 3]
        self.assertEqual(graphs.deep_find(self.d, key), result)

    def test_deep_find_iterable(self):
        key = "f"
        result = True
        self.assertEqual(graphs.deep_find(self.data, key), result)

    def test_deep_find_value_is_list_with_dict(self):
        key = "z"
        result = "Z"
        self.assertEqual(graphs.deep_find(self.data, key), result)

    def test_deep_find_all_shoud_return_all_values_of_given_key(self):
        key = "a"
        result = [10, 20, 30]
        self.assertEqual(graphs.deep_find_all(self.data_all, key), result)

    def test_deep_find_all(self):
        key = "b"
        result = [{"a": 20}, [{"a": 30}]]
        self.assertEqual(graphs.deep_find_all(self.data_all, key), result)

    def test_deep_find_all_with_no_key_found(self):
        key = "Z"
        result = []
        self.assertEqual(graphs.deep_find_all(self.data_all, key), result)

    def test_deep_update_first_level_key(self):
        graphs.deep_update(self.data_all, "a", 50)
        self.assertEqual(self.data_all["a"], 50)

    def test_deep_update_deep_inside(self):
        graphs.deep_update(self.data_all, "a", 50)
        self.assertEqual(self.data_all["a"], 50)
        self.assertEqual(self.data_all["b"]["a"], 50)
        self.assertEqual(self.data_all["c"][0]["b"][0]["a"], 50)

    def tearDown(self):
        self.data_all = {
            "a": 10,
            "b": {"a": 20},
            "c": [
                {"b": [{"a": 30}]}
            ]
        }


if __name__ == "__main__":
    unittest.main()
