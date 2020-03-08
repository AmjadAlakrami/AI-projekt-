import json
import cv2
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
import os
import yolo


DEFAULT_CONFIG_FILE = os.path.join("C:/Users/amjad/OneDrive/Desktop/AI-projekt-/image_det", "config.json")
DEFAULT_WEIGHT_FILE = os.path.join("C:/Users/amjad/OneDrive/Desktop/AI-projekt-/image_det", "Model.h5")
DEFAULT_THRESHOLD = 0.7



if __name__ == '__main__':

    with open(DEFAULT_CONFIG_FILE) as config_buffer:
        config = json.loads(config_buffer.read())

    # 2. create yolo instance & predict
    yolo = create_yolo(config['model']['architecture'],
                       config['model']['labels'],
                       config['model']['input_size'],
                       config['model']['anchors'])
    yolo.load_weights(DEFAULT_WEIGHT_FILE )

    

    cap = cv2.VideoCapture(1)
    while True:
        _,frame = cap.read()
        boxes, probs = yolo.predict(frame, DEFAULT_THRESHOLD)
        labels = np.argmax(probs, axis=1) if len(probs) > 0 else [] 
        # 4. save detection result
        frame = draw_scaled_boxes(frame, boxes, probs, config['model']['labels'])
        label_list = config['model']['labels']
        cv2.imshow("imageo", frame)
        cv2.waitKey(1)
        for x in boxes:
            print(x[1])
    cv2.destroyAllWindows()
            