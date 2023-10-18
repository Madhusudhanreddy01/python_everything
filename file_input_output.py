# name = input("What's your name? ")

# with open("madhu.txt", "a") as file:
#     file.write(f"{name}\n")

# # ----------------------------------

# # import argparse
# # import os


# # def replace_word(task, work, file_path):
# #     """Replaces all instances of a given word in a file with a specific word."""
# #     os.system(f"sed -i 's/{task}/{work}/g' {file_path}")


# # if __name__ == "__main__":
# #     parser = argparse.ArgumentParser(description="Replace a given word with a specific word in a file.")
# #     parser.add_argument("--task", help="The word to replace.", required=True)
# #     parser.add_argument("--work", help="The word to replace the old word.", required=True)
# #     parser.add_argument("--word.txt", help="The path of the file to perform the replacement on.", required=True)
# #     args = parser.parse_args()

# #     replace_word(args.task, args.work, args.word.txt)




import os
import tempfile
import unittest

from replace_word import replace_word

class TestReplaceWord(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with a specific word
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b"Hello world\n")
        self.temp_file.write(b"Hello universe\n")
        self.temp_file.close()

    def tearDown(self):
        # Delete the temporary file
        os.remove(self.temp_file.name)

    def test_replace_word(self):
        # Replace the word in the temporary file
        replace_word(self.temp_file.name, "world", "python")

        # Verify that the word has been replaced correctly
        with open(self.temp_file.name, "r") as f:
            lines = f.readlines()
            self.assertEqual(lines[0], "Hello python\n")
            self.assertEqual(lines[1], "Hello universe\n")

if __name__ == "__main__":
    unittest.main()



