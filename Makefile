dependencies:
    sudo apt-get install -y \
        python3-pip \
        build-essential \
        git \
        python3 \
        python3-dev \
        ffmpeg \
        libsdl2-dev \
        libsdl2-image-dev \
        libsdl2-mixer-dev \
        libsdl2-ttf-dev \
        libportmidi-dev \
        libswscale-dev \
        libavformat-dev \
        libavcodec-dev \
        zlib1g-dev

requirements:
	pip install -r requirements-cython.txt
	pip install -r requirements.txt