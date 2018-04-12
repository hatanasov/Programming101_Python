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
        pass

# class Xmlable:
#     def to_xml():
#         pass


#     @classmethod
#     def from_xml(cls, xml_string):
#         pass


