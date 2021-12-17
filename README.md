# pyqt-notifier
PyQt Windows notifier show at bottom right of the desktop screen

## Requirements
PyQt5 >= 5.8

## Included package
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Usage
```python
notifierWidget = NotifierWidget(informative_text: str, detailed_text: str) # Informative text is large text at upper part of the notifier window and detailed text is small text at lower part.  
notifierWidget.addWidgets(widgets: list) # You can add some widgets at the bottom of the notifier. Note: This needs more tests.
```

## Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_notifier import NotifierWidget

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    notifierWidget = NotifierWidget()
    notifierWidget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/146488175-1041ade0-4263-4f2c-a208-fa6105f73ec2.png)
