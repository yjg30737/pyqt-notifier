from setuptools import setup, find_packages

setup(
    name='pyqt-notifier',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_notifier.style': ['button.css'], 'pyqt_notifier.ico': ['close.svg']},
    description='PyQt Windows notifier show at bottom right of the desktop screen',
    url='https://github.com/yjg30737/pyqt-notifier.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)