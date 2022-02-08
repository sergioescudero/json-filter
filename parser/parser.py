import json
import os


class FilePathMixin:

    def get_absolute_path(self, relative_path):
        return os.path.join(self.__get_parent_dir(), relative_path)

    def __get_parent_dir(self):
        return os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


class FileParser(FilePathMixin):

    def read_json_from_file(self, path):
        with open(self.get_absolute_path(path), "r") as json_file:
            try:
                return json.load(json_file)
            except ValueError as error:
                raise error

    def read_json_from_csv(self, path):
        raise NotImplementedError('To be done')
