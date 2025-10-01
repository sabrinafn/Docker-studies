ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    libglfw3-dev \
    libx11-dev \
    libxext-dev \
    libxft-dev \
    libxrandr-dev \
    libxi-dev \
    libopenal-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/codam-coding-college/MLX42.git ./MLX42 \
    && cmake ./MLX42 -B ./MLX42/build \
    && make -C ./MLX42/build -j4

COPY app/ ./

RUN make -C /app

CMD ["/bin/sh"]
