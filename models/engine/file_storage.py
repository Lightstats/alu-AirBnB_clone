import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        class_key = (type(obj).__name__) + "." + obj.id
        self.__objects[class_key] = obj

    def save(self):
        json_object = json.dumps(self.__objects, indent=4)

        with open(self.__file_path, "w") as outfile:
            outfile.write(json_object)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, "r") as openfile:
                self.__objects = json.load(openfile)
