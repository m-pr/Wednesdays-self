

class ANewClass:
    a_class_attribute = list()

    def instance_meth(self):
        self.an_instance_attribute = 1

    @classmethod
    def class_meth(cls):
        pass

    @staticmethod
    def static_meth():
        pass


def class_attributes():
    an_obj = ANewClass()
    another= ANewClass()
    print(an_obj.a_class_attribute,another.a_class_attribute, "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
    an_obj.a_class_attribute.append(1)
    print(an_obj.a_class_attribute,another.a_class_attribute, "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
    an_obj.a_class_attribute = []
    print(an_obj.a_class_attribute,another.a_class_attribute,  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
    an_obj.a_class_attribute =[1]
    print(an_obj.a_class_attribute,another.a_class_attribute,  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )

if __name__ == '__main__':
        class_attributes()
