# Используем базовый образ PyTorch с поддержкой CUDA
FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    cmake \
    build-essential \
    libprotobuf-dev \
    protobuf-compiler \
    libboost-all-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install transformers flask sentencepiece tokenizers

WORKDIR /app

COPY run_gpt_neo_pipeline.py /app/run_gpt_neo_pipeline.py

ENV HUGGINGFACE_TOKEN={kee}

CMD ["python", "run_gpt_neo_pipeline.py"]