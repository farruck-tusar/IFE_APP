import sys
import torch
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from yolov5.models.experimental import attempt_load
from yolov5.utils.general import non_max_suppression
from yolov5.utils.datasets import LoadImages
from yolov5.utils.torch_utils import select_device, time_synchronized


class YOLOv5App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YOLOv5 Object Detection")
        self.setGeometry(100, 100, 800, 600)

        self.button = QPushButton("Detect Objects", self)
        self.button.setGeometry(10, 10, 150, 50)
        self.button.clicked.connect(self.detect_objects)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 70, 400, 400)

        self.scene = QGraphicsScene()
        self.result_view = QGraphicsView(self)
        self.result_view.setGeometry(420, 70, 370, 400)
        self.result_view.setScene(self.scene)

    def detect_objects(self):
        options = {
            "weights": "yolov5s.pt",
            "img-size": 640,
        }

        device = select_device("")
        model = attempt_load("yolov5s.pt", map_location=device)
        model.eval()

        # Use a file dialog to select an image for detection
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)

        if file_name:
            img = LoadImages(file_name, img_size=options['img-size'])[0]
            img = img.to(device)

            with torch.no_grad():
                pred = model(img)

            pred = non_max_suppression(pred, conf_thres=0.5, iou_thres=0.5)[0]

            # Process and display the detected objects
            if pred is not None:
                image_data = pred[0]
                image = img[0].cpu().numpy().transpose(1, 2, 0)  # Convert image to numpy format

                for obj in image_data:
                    x1, y1, x2, y2, conf, class_id = obj

                    # Draw bounding box on the image
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

                    # Display class label and confidence
                    label = f"Class: {int(class_id)}, Confidence: {conf:.2f}"
                    cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Convert the image back to QPixmap for displaying in the GUI
                height, width, channel = image.shape
                bytes_per_line = 3 * width
                q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)

                # Display the processed image with bounding boxes in the GUI
                self.image_label.setPixmap(pixmap)
                self.image_label.setScaledContents(True)

                # Display the same image in the QGraphicsView
                pixmap_item = QGraphicsPixmapItem(pixmap)
                self.scene.clear()
                self.scene.addItem(pixmap_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YOLOv5App()
    window.show()
    sys.exit(app.exec_())
