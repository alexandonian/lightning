from lightning import readers as reader
from lightning.resources import values


print(reader.listsubdir('resources/images'))
print(reader.listsubdirflat('resources/images'))
