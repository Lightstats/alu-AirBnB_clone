import uuid
from __init__ import storage
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                format_string = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at":
                    self.__dict__[key] = datetime.strptime(
                        value, format_string)
                elif key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, format_string)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        return model_dict


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)

my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))
