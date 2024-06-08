# Dynamic Flow Layout
This custom layout, compatible with PyQt, PySide, and QtPy applications, offers dynamic resizing to seamlessly fill the parent widget without leaving irregular margins. It ensures items within the layout self-adjust to fill the margins of the parent widget when needed, providing a smooth and cohesive user interface experience.

## Images

### Dynamic Flow Layout
![Screenshot 2024-06-08 054934](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/41fcd0d5-4899-4ca1-80e8-2c9b85269c83)
![Screenshot 2024-06-08 054748](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/1dd4c04b-2a03-48d7-ac62-0c8f84c69ce3)
![Screenshot 2024-06-08 054813](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/4feec973-8424-4bcc-a86e-fe56ab96f5e5)
![Screenshot 2024-06-08 054851](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/b3293684-1010-4888-bc49-f523a6773ac2)
<br><br>
### Flow Layout
![Screenshot 2024-06-08 054431](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/c06a6b9c-e1cd-4f00-8a78-e8a20a3b2818)
![Screenshot 2024-06-08 054459](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/bd46b1c6-c0a5-4c90-ac9f-497224be5f6f)
![Screenshot 2024-06-08 054536](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/1a868d8c-9d8c-4c02-a9de-50fee6f8f087)
![Screenshot 2024-06-08 054636](https://github.com/chinmaykrishnroy/PyQt5DynamicFlowLayout/assets/65699140/57016c57-82a2-4da3-b61e-a24c9fc866dd)


## Key Differences

- **Initialization**:
  - **FlowLayout**: Requires parameters for `parent` and `spacing`.
  - **DynamicFlowLayout**: Extends functionality by accepting parameters for `parent`, `orientation`, `margin`, and `spacing`.

- **Item Management**:
  - **FlowLayout**: Manages items via a list named `items`.
  - **DynamicFlowLayout**: Implements item management through a list named `itemList`.

- **Expanding Directions**:
  - **FlowLayout**: Expands both horizontally and vertically.
  - **DynamicFlowLayout**: Unlike FlowLayout, it doesn't expand in any direction (`Qt.Orientation(0)`).

- **Geometry Management**:
  - **FlowLayout**: Utilizes `setGeometry` alongside the `_doLayout` method to arrange items within the given rectangle.
  - **DynamicFlowLayout**: Enhances layout control with `setGeometry` and `doLayout` methods, ensuring orientation and wrapping are respected as needed.

- **Size Calculation**:
  - **FlowLayout**: Utilizes `minimumSize` and `_calculateSize` methods to determine the minimum required size.
  - **DynamicFlowLayout**: Employs `minimumSize` and `doLayout` methods to dynamically adjust layout size based on width or height, depending on orientation.

- **Orientation Support**:
  - **FlowLayout**: Assumes a grid layout without explicit orientation handling.
  - **DynamicFlowLayout**: Offers explicit support for both horizontal and vertical orientations, providing methods such as `hasHeightForWidth` and `hasWidthForHeight`.

This comparison highlights the distinct functionalities of the two custom layout classes, aiding in choosing the appropriate one based on specific UI requirements.

# Choosing Between FlowLayout and DynamicFlowLayout

When faced with selecting between the `FlowLayout` and `DynamicFlowLayout` classes for PyQt5 applications, consider the following factors:

## FlowLayout

- **Suitability**: Suited for simpler layouts where items are arranged horizontally or vertically with minimal dynamic adjustment.
- **Functionality**: Provides basic functionality for arranging items in a straightforward flow, ideal for uncomplicated UI designs.
- **Use Case**: Appropriate for applications with relatively static layouts, where items don't require dynamic adjustments or wrapping.

## DynamicFlowLayout

- **Suitability**: Offers increased flexibility and control, allowing items to dynamically adjust and wrap based on available space.
- **Functionality**: Provides dynamic adjustment and wrapping of items, crucial for accommodating changes in screen size or user interaction.
- **Use Case**: Ideal for complex layouts where items may need to wrap to the next line or column to cater to varying screen sizes or user preferences.

## Conclusion

Select `FlowLayout` for layouts requiring simple, static arrangement of items in horizontal or vertical flows. Opt for `DynamicFlowLayout` when anticipating the need for dynamic adjustments and wrapping of items, especially in response to changes in screen size or user interaction.

Evaluate the complexity of your UI design and the required level of flexibility and responsiveness to determine the most suitable layout class for your application's needs.
