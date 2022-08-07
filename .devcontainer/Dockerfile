FROM ubuntu as base
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        make cmake g++ ca-certificates wget unzip yasm pkg-config \
        libswscale-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev \
        libavformat-dev libpq-dev libxine2-dev libglew-dev libtiff5-dev \
        zlib1g-dev libjpeg-dev libavcodec-dev libavformat-dev libavutil-dev \
        libpostproc-dev libswscale-dev libeigen3-dev libtbb-dev libgtk2.0-dev \
        python3-dev python3-numpy \
    && rm -rf /var/lib/apt/lists/*
RUN cd /tmp \
    && wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip \
    && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip \
    && unzip /tmp/opencv.zip \
    && unzip /tmp/opencv_contrib.zip \
    && rm /tmp/opencv.zip \
    && rm /tmp/opencv_contrib.zip
RUN mkdir /tmp/build \
    && cd /tmp/build \
    && cmake \
        -DOPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib-4.x/modules \
        /tmp/opencv-4.x \
    && cmake --build . --parallel 6 \
    && cmake --install . \
    && rm -r \
        /tmp/opencv-4.x \
        /tmp/opencv_contrib-4.x \
        /tmp/build

FROM base as devel
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install jupyter