from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsRectItem
from typing import Union, Optional

from TBDIC_feature import feature_enabled


class TBDIC_drawer_helper:
    """
    This class contains all the helper functions for the TBDIC_drawer class.
    """

    def __init__(self):
        pass

    def _setColor(
        self,
        pen_size: int = 2,
        color: Union[tuple, Optional[str]] = None
    ) -> QPen:
        """
        This function sets the color of the pen.

        @param color: The color of the pen. (rgb tuple or color name)

        @return: The pen with the color set.
        """

        pen = QPen()
        pen.setWidth(pen_size)

        if color is not None:
            if isinstance(color, tuple):
                pen.setColor(QColor(color[0], color[1], color[2]))
            elif isinstance(color, str):
                pen.setColor(QColor(color))

        return pen

    def _setObject(self):
        pass

    @feature_enabled
    def _imageLoader(self):
        pass

    @feature_enabled
    def _applyRoundedCorners(self, rect_item: QGraphicsRectItem):
        pass
