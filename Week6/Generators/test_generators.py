import unittest
import generators


class TestGenerators(unittest.TestCase):
    def test_chain(self):
        with self.subTest("Test chain function with two lists"):
            iter_1 = [1, 2, 3]
            iter_2 = "abcd"
            result = list(generators.chain(iter_1, iter_2))
            self.assertEqual(result, [1, 2, 3, "a", "b", "c", "d"])


        with self.subTest("Test chain function with emty list"):
            iter_1 = []
            iter_2 = iter_1
            self.assertEqual(list(generators.chain(iter_1, iter_2)), [])


    def test_compress(self):
        result = generators.compress(["Ivo", "Rado", "Panda"], [False, True, True])
        self.assertEqual(list(result), ["Rado", "Panda"])


    def test_cycle(self):
        iterable = [1, 2]
        result = []
        gen = generators.cycle(iterable)
        for i in range(100):
            result.append(next(gen))

        self.assertEqual(result, [iterable] * 100)


if __name__ == "__main__":
    unittest.main()