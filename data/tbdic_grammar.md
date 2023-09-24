# TBDIC Grammar

## Introduction

This document outlines the grammar and the various elements used in the Text-Based Diagram Creator (TBDiC). The language is designed to be simple yet powerful, enabling users to create diagrams using text commands. Elements like rectangles, circles, and lines can be created, customized, and connected. Each element comes with its own set of attributes, such as size, position, and color, allowing for a high degree of customization. The grammar rules are described using mathematical notation to provide a formal understanding of the language.

</br>

## Rectangle

A rectangle is a shape with four sides and four right angles.</br>
The rectangle can have a size attribute, a rounded or sharp edges attribute, a color attribute, a position attribute, a rotation attribute, and a content attribute.

### Rectangle Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| Size | `list` | Size of the rectangle (x1, y1, x2, y2) |
| Rounded edges | `bool` | Whether the rectangle has rounded edges or not |
| Color | `str` | Color of the rectangle |
| Position | `list` | Position of the rectangle (x, y) |
| Rotation | `float` | Rotation of the rectangle (in degrees) |
| Content | `obj` | Content of the rectangle |

## Circle

A circle is a shape with all points on its boundary equidistant from its center.</br>
The circle can have a size attribute, a color attribute, a position attribute, a rotation attribute, and a content attribute.

### Circle Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| Size | `float` | Diameter of the circle |
| Color | `str` | Color of the circle |
| Position | `list` | Position of the circle (x, y) |
| Rotation | `float` | Rotation of the circle (in degrees) |
| Content | `obj` | Content of the circle |

## Ellipse

An ellipse is a shape with a curved perimeter.</br>
The ellipse can have a size attribute, a color attribute, a position attribute, a rotation attribute, and a content attribute.

### Ellipse Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| Size | `list` | Size of the ellipse (x, y) |
| Color | `str` | Color of the ellipse |
| Position | `list` | Position of the ellipse (x, y) |
| Rotation | `float` | Rotation of the ellipse (in degrees) |
| Content | `obj` | Content of the ellipse |

## Grammar

In this section, the grammar of the TBDiC language is described using LaTeX notation. The grammar is described using the following rules:
</br>

### Elements

$$
\begin{align}
    \text{Elements} &\to
    \begin{cases}
        Circle \\
        Ellipse \\
        Rectangle &\to
        \begin{cases}
            \text{rounded\underline{ }edges} \\
            \text{sharp\underline{ }edges}
        \end{cases} \\
        Arrow
    \end{cases} \\

    \text{Element attributes} &\to
    \begin{cases}
        Size \\
        Color \\
        Position \\
        Rotation \\
        Content
    \end{cases} \\

    \text{Content} &\to
    \begin{cases}
        Text &\to
        \begin{cases}
            Text\space content \\
            Font \\
            Font\space size \\
            Font\space color
        \end{cases} \\
        Image &\to
        \begin{cases}
            Image\space path \\
            Image\space size\space (\text{preferred})
        \end{cases} \\
        Hyperlink &\to
        \begin{cases}
            Hyperlink\space URL \\
            Hyperlink\space text
        \end{cases} \\
    \end{cases}
\end{align}
$$

### Commands

$$
\begin{align}
    \text{Commands} &\to
    \begin{cases}
        \text{create} \\
        \text{modify} \\
        \text{connect} \\
        \text{delete} \\
    \end{cases} \\
\end{align}
$$

#### Command Reference

$$
\begin{align}
    \text{create} &\to
    \begin{cases}
        \text{create\underline{ }element} \\
        \text{create\underline{ }attribute}
    \end{cases} \\

    \text{modify} &\to
    \begin{cases}
        \text{modify\underline{ }element} \\
        \text{modify\underline{ }attribute}
    \end{cases} \\

    \text{connect} &\to
    \begin{cases}
        \text{connect\underline{ }element} \\
        \text{connect\underline{ }attribute}
    \end{cases} \\

    \text{delete} &\to
    \begin{cases}
        \text{delete\underline{ }element} \\
        \text{delete\underline{ }attribute}
    \end{cases} \\

    \text{create\underline{ }element} &\to
    \begin{cases}
        \text{create\underline{ }circle} \\
        \text{create\underline{ }ellipse} \\
        \text{create\underline{ }rectangle} \\
        \text{create\underline{ }arrow}
    \end{cases} \\

    \text{create\underline{ }attribute} &\to
    \begin{cases}
        \text{create\underline{ }size} \\
        \text{create\underline{ }color} \\
        \text{create\underline{ }position} \\
        \text{create\underline{ }rotation} \\
        \text{create\underline{ }content}
    \end{cases} \\

    \text{modify\underline{ }element} &\to
    \begin{cases}
        \text{modify\underline{ }circle} \\
        \text{modify\underline{ }ellipse} \\
        \text{modify\underline{ }rectangle} \\
        \text{modify\underline{ }arrow}
    \end{cases} \\
\end{align}
$$

##### Create

The create command is used to create elements and attributes.
___

###### Create Element

Shows the syntax for creating an element by an example of creating different elements.

Circle:

$$
\begin{align}
    \text{create\underline{ }circle} &\to \text{create\underline{ }circle(10, red, (25, 60), 0)} \\
\end{align}
$$

- 10: Size
- red: Color
- (25, 60): Position
- 0: Rotation
- Content: None

</br>
Ellipse:

$$
\begin{align}
    \text{create\underline{ }ellipse} &\to \text{create\underline{ }ellipse(10, 20, red, (25, 60), 0, 0)} \\
\end{align}
$$

- 10: Size x
- 20: Size y
- red: Color
- (25, 60): Position
- 0: Rotation
- 0: Content

</br>
Rectangle:

$$
\begin{align}
    \text{create\underline{ }rectangle} &\to \text{create\underline{ }rectangle(True, red, (25, 60, 50, 100), 0, 0)} \\
\end{align}
$$

- True: Rounded edges
- red: Color
- (25, 60, 50, 100): Position (x1, y1, x2, y2)
- 0: Rotation
- 0: Content

</br>

##### Connect

The connect command is used to connect elements and attributes together.
For a connection one could choose between a line or an arrow.

$$
\begin{align}
    \text{connect\underline{ }element} &\to
    \begin{cases}
        \text{connect\underline{ }line} \\
        \text{connect\underline{ }arrow}
    \end{cases} \\
\end{align}
$$

___

###### Connect Line

Shows the syntax for connecting elements with a line by an example of connecting different elements.

$$
\begin{align}
    \text{connect\underline{ }line} &\to \text{connect\underline{ }line(circle1, circle2, [line, red, top\underline{ }middle])} \\
\end{align}
$$

- circle1: Element 1
- circle2: Element 2
- line: Type (line, arrow)
- red: Color
- middle: Position (top, middle, bottom)
  - Each element could be connected to the middle, or edge

</br>

###### Connect Arrow

$$
\begin{align}
    \text{connect\underline{ }arrow} &\to \text{connect\underline{ }arrow(circle1, circle2, [line, red, top\underline{ }middle])} \\
\end{align}
$$

- circle1: Element 1
- circle2: Element 2
- line: Type (line, arrow)
- red: Color
- middle: Position (top, middle, bottom)
  - Each element could be connected to the middle, or edge
