SUBJECT=$1
SESSIONNAME=$2
cd $HOME/DATA_COLLECTION/$SUBJECT/$SESSIONNAME
LATEST_REC=$(echo $(ls -Art | tail -1))
echo ************************GPS*************************
cd $HOME/DATA_COLLECTION/$SUBJECT/$SESSIONNAME/$LATEST_REC/gps
rosbag info $(echo $(ls -t | grep .bag | sort -n |tail -2|head -1))

echo **********************CAMERA-1************************
cd $HOME/DATA_COLLECTION/$SUBJECT/$SESSIONNAME/$LATEST_REC/images1/
rosbag info $(echo $(ls -t | grep .bag | sort -n |tail -2|head -1))

echo **********************CAMERA-2************************
cd $HOME/DATA_COLLECTION/$SUBJECT/$SESSIONNAME/$LATEST_REC/images2/
rosbag info $(echo $(ls -t | grep .bag | sort -n |tail -2|head -1))

echo **********************CAMERA-3************************
cd $HOME/DATA_COLLECTION/$SUBJECT/$SESSIONNAME/$LATEST_REC/images3/
rosbag info $(echo $(ls -t | grep .bag | sort -n |tail -2|head -1))

echo **********************CAMERA-4************************
cd $HOME/DATA_COLLECTION/$SUBJECT/$SESSIONNAME/$LATEST_REC/images4/
rosbag info $(echo $(ls -t | grep .bag | sort -n |tail -2|head -1))

echo **********************CAN-MESSAGES************************
python3 $HOME/data_collection_scripts/get_can_bus_recording_size.py $SUBJECT $SESSIONNAME
# cd $HOME/DATA_COLLECTION/$SUBJECT/$LATEST_REC/can/
# stat -c "%s" $(echo $(ls -t | grep .csv ))
