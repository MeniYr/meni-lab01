class SinglrtonClass(object):
     _insance = None

     def __new__(cls):
         if cls._insance is None:
             print('Creating the object')
             cls._insance = super(SinglrtonClass, cls).__new__(cls)
         return cls._insance