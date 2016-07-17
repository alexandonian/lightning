from lightning import series, image
from lightning.image.controller import ImageController, Provider
from lightning.image.readers import fromarray
from lightning.resources.values import Types
import numpy as np
from lightning_flash import image

tma = Provider()
print('ImageSetProvider: ')
print(tma)
print('Modalities: ')
print(tma.project_info.keys())
print(tma.project_info[Types.IF].items())

