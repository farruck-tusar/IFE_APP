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