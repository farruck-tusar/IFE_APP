# IFE APPLICATION
> **IFE**, which stands for Intelligent Frame Extractor, is a software application that was developed by the Chair of Computer Engineering to support the different projects under study at the IFC (Indoor Flight Center).
> 
> **IFE** is a data processing tool that is used for the processing of video frames using different object detection algorithms. The results of the processing are saved by the mean of data serialization techniques.

# Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6".

**Windows**:
```console
python main.py
```
**MacOS and Linux**:
```console
python3 main.py
```
# Compiling
```console
python setup.py build
```

# Project Files And Folders
> **main.py**: application initialization file
> 
> **mainwindow.ui**: Qt Designer project.
> ```console
> pyside6-uic mainwindow.ui> mainwindow.py 
> ```
> 
> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. "resource.qrc" file compiled for python using the command:
> ```console
> pyside6-rcc resources.qrc -o resources_rc.py
> ```

# Integrate YOLO
**YOLOv5**: cloning and installing requirements

> git clone https://github.com/ultralytics/yolov5

> cd yolov5

> pip install -U -r requirements.txt


# Packaging(cx_Freeze)
***cx_Freeze*** normally produces a folder containing an executable file for your program, along with the shared libraries (DLLs or .so files) needed to run it. You can make a simple Windows installer using a setup script with the bdist_msi option, or a Mac disk image with bdist_dmg.

Details: https://cx-freeze.readthedocs.io/en/6.10/index.html

***Installation***

In a virtual environment, install by issuing the command:

> pip install --upgrade cx_Freeze

***Commands***
> python setup.py build

> python setup.py bdist_msi

*On Mac OS X, we can use bdist_dmg to build a Mac disk image. It creates an application bundle, then packages it into a DMG disk image suitable for distribution and installation.

> python setup.py bdist_mac

*This command is available on Mac OS X systems, to create a Mac application bundle (a .app directory).
