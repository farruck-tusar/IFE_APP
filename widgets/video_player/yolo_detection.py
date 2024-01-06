import logging
import os
import subprocess
import sys

from application import Settings
from yolov5 import detect


class YoloDetection():
    def yolov5_detect(video_path):
        venv_directory = os.path.join(Settings.VENV_DIR, "_yolov5")

        activate_script = 'bin/activate' if sys.platform != 'win32' else 'Scripts\\activate'
        venv_activate_script = os.path.join(venv_directory, activate_script)

        python_path = 'bin/python' if sys.platform != 'win32' else 'Scripts\\python'
        venv_python_path = os.path.join(venv_directory, python_path)

        logging.info("[START] venv activation")
        activate_cmd = f'source {venv_activate_script}' if sys.platform != 'win32' else venv_activate_script
        subprocess.run(activate_cmd, shell=True)
        logging.info("[END] venv activation")

        logging.info("[START] YOLOv5 detection")
        detect.run(source=video_path,
                   weights=os.path.join(Settings.YOLO_WEIGHT_DIR),
                   project=os.path.join(Settings.OUTPUT_DIR, Settings.OUTPUT_FOLDER_NAME),
                   conf_thres=0.5,
                   save_txt=True)
        logging.info("[END] YOLOv5 detection")

        logging.info("[START] venv deactivation")
        if sys.platform == 'win32':
            subprocess.run('deactivate', shell=True)
        else:
            subprocess.run('deactivate', shell=True)
        logging.info("[END] venv deactivation")

    def yolov8_detect(video_path):
        venv_directory = os.path.join(Settings.VENV_DIR, "_yolov8")

        activate_script = 'bin/activate' if sys.platform != 'win32' else 'Scripts\\activate'
        venv_activate_script = os.path.join(venv_directory, activate_script)

        python_path = 'bin/python' if sys.platform != 'win32' else 'Scripts\\python'
        venv_python_path = os.path.join(venv_directory, python_path)

        logging.info("[START] venv activation")
        activate_cmd = f'source {venv_activate_script}' if sys.platform != 'win32' else venv_activate_script
        subprocess.run(activate_cmd, shell=True)
        logging.info("[END] venv activation")

        logging.info("[START] YOLOv8 detection")
        detect.run(source=video_path,
                   weights=os.path.join(Settings.YOLO_WEIGHT_DIR),
                   project=os.path.join(Settings.OUTPUT_DIR, Settings.OUTPUT_FOLDER_NAME),
                   conf_thres=0.5,
                   save_txt=True)
        logging.info("[END] YOLOv8 detection")

        logging.info("[START] venv deactivation")
        if sys.platform == 'win32':
            subprocess.run('deactivate', shell=True)
        else:
            subprocess.run('deactivate', shell=True)
        logging.info("[END] venv deactivation")