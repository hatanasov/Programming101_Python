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
                {"b": [{"a": 30}, {"b": 40}]}
            ]
        }

    def test_deep_find_no_key_found(self):
        key = "X"
        self.assertEqual(graphs.deep_find(self.data, key), None)

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
        result = [{"a": 20}, [{"a": 30}, {"b": 40}]]
        self.assertEqual(graphs.deep_find_all(self.data_all, key), result)

    def test_deep_find_all_with_no_key_found(self):
        key = "Z"
        result = []
        self.assertEqual(graphs.deep_find_all(self.data_all, key), result)

    def test_deep_update_all_elements(self):
        result = {'a': 10, 'b': 20, 'c': [{'b': 20}]}
        self.assertEqual(graphs.deep_update(self.data_all, "b", 20), result)

    def test_deep_update_deep_inside(self):
        result = {'a': 100, 'b': {'a': 100},
                  'c': [{'b': [{'a': 100}, {'b': 40}]}]}
        self.assertEqual(graphs.deep_update(self.data_all, "a", 100), result)

    def test_deep_update(self):
        data = {"a": [[[[[{"b": 100, "b": 10}, ({"b": []})]]]]]}
        result = {"a": [[[[[{"b": True, "b": True}, ({"b": True})]]]]]}
        self.assertEqual(graphs.deep_update(data, "b", True), result)
        self.assertEqual(
            data, {"a": [[[[[{"b": 100, "b": 10}, ({"b": []})]]]]]})

    def tearDown(self):
        self.data_all = {
            "a": 10,
            "b": {"a": 20},
            "c": [
                {"b": [{"a": 30}, {"b": 40}]}
            ]
        }


if __name__ == "__main__":
    unittest.main()
