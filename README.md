# pyqt-notifier
PyQt Windows notifier show at bottom right of the desktop screen

## Requirements
PyQt5 >= 5.8

## Included package
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a> - For svg icon close button

## Setup
`python -m pip install pyqt-notifier`

## Usage
```python
# Informative text is large text at upper part of the notifier window and detailed text is small text at lower part.  
notifierWidget = NotifierWidget(informative_text: str, detailed_text: str)
# You can add some widgets at the bottom of the notifier. Note: This needs more tests.
notifierWidget.addWidgets(widgets: list) 
```

If you press the escape button or click the exit button on the top right of the notifier window, notifier window will be closed.

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

![image](https://user-images.githubusercontent.com/55078043/158148559-8a159186-da37-4cd7-af37-d26c3f30e79f.png)
