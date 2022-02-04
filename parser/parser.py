import json
import os


class FilePathMixin:

    def get_absolute_path(self, relative_path):
        parent_dir = self.__get_parent_dir()
        return os.path.join(parent_dir, relative_path)

    def __get_parent_dir(self):
        return os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


class FileParser(FilePathMixin):

    def read_json_from_file(self, path):
        x = self.get_absolute_path(path)
        with open(x, "r") as json_file:
            data = json.load(json_file)
            return data

    def read_json_from_csv(self, path):
        raise NotImplementedError('To be done')
