from abc import ABC, abstractmethod
import pytest

class ANewClass:
    a_class_attribute = list()
    _cls_property = []

    def __init__(self):
        self.an_instance_attribute = 1
        self._instance_property = 1 #same so far
        
    def _get_instance_property(self):
        print(f"getting property {self._instance_property}")
        return self._instance_property
    def _set_instance_property(self,new_value):
        print(f"setting property - old value: ")
        #old = self._instance_property does not work nor dose self.instance_property
        pprint(dir(self))
        self._instance_property = new_value
    def _del_instance_property(self):
        print("deleting property")
        del self._instance_property

    instance_property = property(
        fget=_get_instance_property,
        fset=_set_instance_property,
        fdel=_del_instance_property,
        doc="The an instance property is different from a attribute"
    )

    def _get_cls_property(cls):
        print(f"getting property {self._instance_property}")
        return cls._cls_property
    def _set_cls_property(cls,new_value):
        print(f"setting property")
        #old = self._instance_property does not work nor dose self.instance_property
        pprint(dir(self))
        cls._cls_property = new_value
    def _del_cls_property(cls):
        print("deleting property")
        del cls._cls_property
    cls_property = property(
        fget=_get_cls_property,
        fset=_set_cls_property,
        fdel=_del_cls_property,
        doc="a class property?"
    )
    


    def instance_meth(self):
        self._instance_property +=1
        print("instance meth")
    @classmethod
    def class_meth(cls):
        print("class meth")

    @staticmethod
    def static_meth():
        print("static meth")


class AnAbstractClass(ABC):
    
    @abstractmethod
    def implementMe(self):
        #print("unimplemented")
        ...

class ASubclass(AnAbstractClass):

    def __init__(self):
        self.att = 1
    def implementMe(self):
        super().implementMe()
        print("implemented")

if __name__ == '__main__':
    from pprint import pprint
    

    def class_attributes():
        an_obj = ANewClass()
        another= ANewClass()
        print(f"an_obj:{an_obj.a_class_attribute}, another:{another.a_class_attribute}, class:{ANewClass.a_class_attribute}. instances: ",  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
        an_obj.a_class_attribute.append(1)
        print(f"an_obj:{an_obj.a_class_attribute}, another:{another.a_class_attribute}, class:{ANewClass.a_class_attribute}. instances: ",  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
        an_obj.a_class_attribute = []
        print(f"an_obj:{an_obj.a_class_attribute}, another:{another.a_class_attribute}, class:{ANewClass.a_class_attribute}. instances: ",  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
        an_obj.a_class_attribute =[1]
        print(f"an_obj:{an_obj.a_class_attribute}, another:{another.a_class_attribute}, class:{ANewClass.a_class_attribute}. instances: ",  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
        ANewClass.a_class_attribute.append(2)
        print(f"an_obj:{an_obj.a_class_attribute}, another:{another.a_class_attribute}, class:{ANewClass.a_class_attribute}. instances: ",  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )
        another.a_class_attribute = [3]
        ANewClass.a_class_attribute.append(4)
        print(f"an_obj:{an_obj.a_class_attribute}, another:{another.a_class_attribute}, class:{ANewClass.a_class_attribute}. instances: ",  "Same Object" if another.a_class_attribute is an_obj.a_class_attribute else "Different Object" )


    def properties():
        an_obj = ANewClass()
        an_obj.a_class_attribute.append(2)
        an_obj.an_instance_attribute = 2
        an_obj.instance_property = 2
        print(an_obj.instance_property)

    def methods():
        an_obj = ANewClass()
        an_obj.class_meth()
        ANewClass.class_meth()
        an_obj.static_meth()
        ANewClass.static_meth()
        an_obj.instance_meth()
        ANewClass.instance_meth(an_obj)  #odd but it works
        print(an_obj.instance_property)

    def abstact_classes():
        # um = AnAbstractClass()
        de = ASubclass()
        de.implementMe()
        ...

    class_attributes()
    print("——————————————————————————————————————————")
    properties()
    print("——————————————————————————————————————————")
    methods()
    print("——————————————————————————————————————————")
    abstact_classes()
