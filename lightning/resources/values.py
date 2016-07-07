"""
values.py

Strings - Contains important string keywords used throughout the application.
Paths   - Contains important paths that define data directory locations.
"""


class Types(object):
    """
    # TODO!!
    """
    # Imaging Types/Modalities:

    IF = 'IF'
    WSI = 'WSI'
    IHC = 'IHC'
    HaE = 'HaE'
    IMS = 'IMS'
    ISH = 'ISH'


class Paths(object):
    """
    # TODO
    """

    # Important paths that define where the data directories are stored relative
    # to base/src directories
    IF_data = '../../test/resources/data'
    IF_images = '../../test/resources/images'


Project_info = {
    Types.IF: {'images': Paths.IF_images,
               'data': Paths.IF_data}
}
