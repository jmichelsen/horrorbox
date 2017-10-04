# horrorbox

# instal packages
$ sudo apt-get install build-essential cmake pkg-config
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
$ sudo apt-get install libgtk2.0-dev
$ sudo apt-get install libatlas-base-dev gfortran
$ sudo apt-get install python2.7-dev

# install pip and virtualenv
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo pip install virtualenv virtualenvwrapper
$ vi ~/.profile
    # virtualenv and virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
$ source ~/.profile
$ mkvirtualenv horrorbox

# ffmpeg install
$ git clone https://github.com/FFmpeg/FFmpeg.git
cd ffmpeg
sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make
sudo make install

# download and install opencv
$ pip install numpy
$ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.0.0.zip
$ unzip opencv.zip
$ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.0.0.zip
$ unzip opencv_contrib.zip
$ cd ~/opencv-3.0.0/
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D WITH_V4L=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.0.0/modules \
    -D BUILD_EXAMPLES=ON ..
$ make
$ sudo make install
$ sudo ldconfig
$ ln -s /usr/local/lib/python2.7/site-packages/cv2.so ~/.virtualenvs/horrorbox/lib/python2.7/site-packages/



# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
bcm2835-v4l2


# resources
https://www.jeffreythompson.org/blog/2014/11/13/installing-ffmpeg-for-raspberry-pi/
https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
https://github.com/kratzert/Ubuntu_from_scratch/blob/master/Ubuntu_16_04LTS.md#installing-opencv3

