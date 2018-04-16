import json


class Jsonable:
    serializable_types = (
        int,
        float,
        str,
        list,
        bool,
        dict,
        type(None),
    )

    def prepare_to_serelaze(self):
        class_name = self.__class__.__name__

        dict_ = {}

        for key, value in self.__dict__.items():
            if type(value) in self.serializable_types:
                dict_[key] = value
            elif isinstance(value, Jsonable):
                dict_[key] = value.prepare_to_serelaze()

        return {"class_name": class_name, "dict": dict_}

    def to_json(self, indent=4):
        return json.dumps(self.prepare_to_serelaze(), indent=indent)

    @classmethod
    def from_json(cls, json_string):
        dict_ = json.loads(json_string)
        new_obj = cls()
        for k, v in dict_["dict"].items():
            if type(v) == dict and "class_name" in v:
                # print(new_obj.__class__.__name__)
                # print(v["class_name"])
                if new_obj.__class__.__name__ != dict_["class_name"]:
                    # if v["class_name"] != dict_["class_name"]:
                    raise ValueError
                value_obj = cls()
                for key, value in v["dict"].items():
                    setattr(value_obj, key, value)
                setattr(new_obj, k, value_obj)
            else:
                setattr(new_obj, k, v)
        return new_obj

    def __eq__(self, other):
        if self.__dict__ == other.__dict__ and \
                self.__class__.__name__ == other.__class__.__name__:
            return True
        else:
            return False


# class Xmlable:
#     def to_xml():
#         pass


#     @classmethod
#     def from_xml(cls, xml_string):
#         pass
