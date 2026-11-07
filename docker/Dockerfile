FROM osrf/ros:jazzy-desktop

ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências do ROS2 e da simulação
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-pip \
    python3-pytest \
    git \
    mesa-utils \
    ros-jazzy-ros-gz \
    ros-jazzy-navigation2 \
    ros-jazzy-nav2-bringup \
    ros-jazzy-nav2-minimal-tb3-sim \
    ros-jazzy-slam-toolbox \
    ros-jazzy-nav2-simple-commander \
    ros-jazzy-rviz2 \
    ros-jazzy-xacro \
    && rm -rf /var/lib/apt/lists/*

# Preparar o diretório de trabalho
WORKDIR /workspace

# Configurar ROS2 automaticamente no Bash
RUN echo "source /opt/ros/jazzy/setup.bash" >> /etc/bash.bashrc

# Executar com usuário não privilegiado
USER 1000:1000

# Manter o contêiner em execução
CMD ["sleep", "infinity"]

