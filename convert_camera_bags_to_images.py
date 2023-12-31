import os
import rosbag
import cv2
from cv_bridge import CvBridge, CvBridgeError


# /home/iac_user/post-process/test/0-Alcohol/29-09-23_13_57_12

# SOURCE_CAMERA_BAG_FOLDER = "/home/iac_user/post-process/test/bag-test"
# SAVE_FOLDER_FOR_CAMERA_IMAGES = '/home/iac_user/post-process/test/bag-test-output/images'


# RECORDING_FOLDER_NAME = '22-09-23_15:25:12'

# SOURCE_CAMERA_BAG_FOLDER = "/home/iac_user/DATA_COLLECTION/" + RECORDING_FOLDER_NAME
# SAVE_FOLDER_FOR_CAMERA_IMAGES = '/home/iac_user/PROCESSED_DATA_COLLECTION/' + RECORDING_FOLDER_NAME
count = 0
def extract(dirs, filename,topic, output_folder, flipped):
    global count
    bag = rosbag.Bag(os.path.join(dirs, filename))

    for (topic, msg, t) in bag.read_messages():
        bridge = CvBridge()
        try:
            cv_img = bridge.compressed_imgmsg_to_cv2(msg)
            print("here")
        except CvBridgeError as e:
            print(e)
            continue
        if flipped:
            cv_img = cv2.flip(cv2.flip(cv_img, 1), 0)
        filename = os.path.join(output_folder, f'frame_{count}_{t}.png')
        print(filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        cv2.imwrite(filename, cv_img)
        print(count)
        count += 1
    bag.close()


if __name__ == '__main__': 
    SUB_FOLDER_NAME = 'Driving backward/'
    # SUB_FOLDER_NAME = 'Driving forward/'
    # SUB_FOLDER_NAME = 'Eye Tracking/'
    # SUB_FOLDER_NAME = 'Parking/'

    SUB_SUB_FOLDER_NAME = 'Driving backward_'
    # SUB_SUB_FOLDER_NAME = 'Driving forward_'
    # SUB_SUB_FOLDER_NAME = 'Eye Tracking_'

    sub_sub_folder_ind_list = [1]

    # SUB_SUB_FOLDER_IND = '3' # TODO: change the subfolder ind

    # IMAGE_FOLDER = 'images' + str(4) + '/'

    # SOURCE_CAMERA_BAG_FOLDER = "/home/iac_user/post-process/Post-SubjectLL/Baseline/only_driving/17-10-23_10-50-24/" + IMAGE_FOLDER + SUB_FOLDER_NAME + SUB_SUB_FOLDER_NAME +SUB_SUB_FOLDER_IND

    # SAVE_FOLDER_FOR_CAMERA_IMAGES = '/home/iac_user/post-process/1017test/Driving/' + SUB_FOLDER_NAME + SUB_SUB_FOLDER_NAME + SUB_SUB_FOLDER_IND

    for i in range(len(sub_sub_folder_ind_list)):

        SUB_SUB_FOLDER_IND = str(sub_sub_folder_ind_list[i])

        image_ind_list = [1,2,3,4]

        for j in range(len(image_ind_list)):
            IMAGE_FOLDER = 'images' + str(image_ind_list[j]) + '/'

            SOURCE_CAMERA_BAG_FOLDER = "/home/iac_user/post-process/Post-SubjectLL/Baseline/only_driving/17-10-23_10-50-24/images" + IMAGE_FOLDER + SUB_FOLDER_NAME + SUB_SUB_FOLDER_NAME +SUB_SUB_FOLDER_IND

            SAVE_FOLDER_FOR_CAMERA_IMAGES = '/home/iac_user/post-process/1017test/Driving/' + SUB_FOLDER_NAME + SUB_SUB_FOLDER_NAME + SUB_SUB_FOLDER_IND
            
            camera_output_folder = SAVE_FOLDER_FOR_CAMERA_IMAGES + "/img" + str(image_ind_list[j])

            camera_topic = '/camera' + str(image_ind_list[j])+ '/usb_cam'+str(image_ind_list[j]) +'/image_raw/compressed' 
            # camera_topic = [camera_topic_str]

            camera_input_folder = SOURCE_CAMERA_BAG_FOLDER

            for (root, dirs, files) in os.walk(camera_input_folder):
                for file in sorted(files):
                    print(file)
                    extract(root, file, camera_topic, camera_output_folder, True)

            print_str = "Image conversion complete for " + camera_output_folder
            print(print_str)
