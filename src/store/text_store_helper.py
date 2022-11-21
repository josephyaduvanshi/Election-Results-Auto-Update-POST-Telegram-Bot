from src.utils.constants import Constants


class TextAppend:
    @staticmethod
    def write_text_append(text: str):
        with open(f"{Constants.main_dir}/src/store/txt.txt", "w") as f:
            f.write(text)
            f.close()

    @staticmethod
    def read_text_append():
        with open(f"{Constants.main_dir}/src/store/txt.txt", "r") as f:
            text = f.read()
            f.close()
            return text
