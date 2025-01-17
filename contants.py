import numpy as np
import enum

DEFAULT_CHROMATICITY = 0.5


class CONVERSION_MATRIX(enum.Enum):
    class XYZ_TO_LMS(enum.Enum):

        # Hunt-Pinter-Estevez P.19 https://moodle2.cs.huji.ac.il/nu19/pluginfile.php/482566/mod_resource/content/0
        # /Lecture%202a%20-%20white%20balance.pdf
        HPE: np.array((
            (0.3897, 0.6889, -0.0786),
            (-0.2298, 1.1834, 0.0464),
            (0.0000, 0.0000, 1.000)))

        # Normalized to D65 https://en.wikipedia.org/wiki/LMS_color_space
        HPE_NORMALIZED: np.array((
            (0.4002, 0.7075, -0.0807),
            (-0.2280, 1.1500, 0.0612),
            (0.0000, 0.0000, 0.9184)))

        # CIECAM97s : np.array((
        #     (0.4002, 0.7075, -0.0807),
        #     (-0.2280, 1.1500, 0.0612),
        #     (0.0000, 0.0000, 0.9184)))
