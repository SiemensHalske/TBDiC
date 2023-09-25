# from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem
from typing import Union, Optional

from TBDIC_feature import feature_enabled
from TBDIC_drawer_helper import TBDIC_drawer_helper


class TBDIC_drawer(TBDIC_drawer_helper):
    """
    This class contains all the functions that draw the diagrams.

    The diagrams are drawn using the PyQt5 library
    in the 'graphicsView_diagramDisplay' widget.
    """

    auto_name_template_line = 'line_{}'
    auto_name_template_arrow = 'arrow_{}'
    auto_name_template_rectangle = 'rectangle_{}'
    auto_name_template_ellipse = 'ellipse_{}'
    auto_name_template_circle = 'circle_{}'
    AUTO_ELEMENT_NAMES = []

    def __init__(self, drawing_area):
        self.drawing_area = drawing_area
        self.scene = QGraphicsScene()
        self.drawing_area.setScene(self.scene)

        self.master_pen = self._setColor(color=(0, 0, 0))

    def _addElementName(self, name: str, auto_name: bool = True) -> bool:
        """
        This function adds an element name to the list of element names.

        @param name: The name of the element.
        @param auto_name: Whether the name should be automatically generated.

        @return: bool - Whether the name was added successfully.
        """
        if auto_name:
            if name.startswith('line'):
                prefix = 'line'
            elif name.startswith('rectangle'):
                prefix = 'rectangle'
            elif name.startswith('circle'):
                prefix = 'circle'
            elif name.startswith('ellipse'):
                prefix = 'ellipse'
            elif name.startswith('arrow'):
                prefix = 'arrow'
            else:
                return False

            # Find the smallest index for the corresponding name
            index = 1
            while f"{prefix}_{index}" in self.AUTO_ELEMENT_NAMES:
                index += 1

            name = f"{prefix}_{index}"

        self.AUTO_ELEMENT_NAMES.append(name)
        return True

    def draw_line(
        self,
        name: str,  # name of the line
        starting_point: tuple,  # starting point of the line
        ending_point: tuple,  # ending point of the line
        color: Union[tuple, Optional[str]] = None  # color of the line
    ) -> None:
        """
        This function draws a line.
        """

        if name is None:
            ack = self._addElementName(name=name)
        else:
            ack = self._addElementName(name=name, auto_name=False)

        if not ack:
            return -1

        # pen = self._setColor(color=color)

        self.scene.addLine(
            starting_point[0],
            starting_point[1],
            ending_point[0],
            ending_point[1],
            self.master_pen
        )

    def draw_arrow(
        self,
        name: str,  # name of the arrow
        starting_point: tuple,  # starting point of the arrow
        ending_point: tuple,  # ending point of the arrow
        color: Union[tuple, Optional[str]] = None  # color of the arrow
    ):
        """
        This function draws an arrow.
        """

        pass

    def draw_rectangle(
        self,
        name: str = "rectangle",
        starting_point: tuple = (0, 0),
        width: int = 0,  # width (rightward x-coordinate)
        height: int = 0,  # heigth (downward y-coordinate)
        rotation: int = 0,  # rotation in degrees
        rounded: bool = False,  # rounded edges or not?
        color: Union[tuple, Optional[str]] = None,  # color of the rectangle
        display_object: list = None  # list of the object to display
    ):
        """
        This function draws a rectangle.
        """

        @feature_enabled
        def rounded_corners_feature_supported(rect_item: QGraphicsRectItem):
            return self._applyRoundedCorners(rect_item)

        if name is None:
            ack = self._addElementName(name=name)
        else:
            ack = self._addElementName(name=name, auto_name=False)

        if not ack:
            return -1

        # Set the color
        # rect_pen = self._setColor(color=color)

        # Create a QGraphicsRectItem
        rect_item = QGraphicsRectItem(
            starting_point[0], starting_point[1], width, height)

        # Set pen (color and other settings)
        rect_item.setPen(self.master_pen)

        # Apply rotation
        if rotation != 0:
            rect_item.setRotation(rotation)

        # Apply rounded corners
        if rounded:
            # You'll have to implement this yourself, QGraphicsRectItem doesn't
            # support it out-of-the-box
            self._applyRoundedCorners(rect_item)

        # Add the item to the scene
        self.scene.addItem(rect_item)
        return 1

    def draw_ellipse(
        self,
        name: str,  # name of the ellipse
        starting_point: tuple,  # starting point of the ellipse
        width: int,  # width of the ellipse
        height: int,  # height of the ellipse
        rotation: int,  # rotation in degrees
        color: Union[tuple, Optional[str]] = None,  # color of the ellipse
        display_object=None  # object to display
    ):
        """
        This function draws an ellipse.
        """

        pass

    def draw_circle(
        self,
        name: str,  # name of the circle
        starting_point: tuple,  # starting point of the circle
        radius: int,  # radius of the circle
        color: Union[tuple, Optional[str]] = None,  # color of the circle
        display_object=None  # object to display
    ):
        """
        This function draws a circle.
        """

        pass
