# ベースは軽量な Python
FROM python:3.11-slim

# 依存パッケージ（OpenCVの実行に必要）
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# pip を最新化
RUN python -m pip install --upgrade pip

# PyTorch (CPU版) を先に入れる
# ※ CPUのみでOK。GPU不要。ARM/Intel どちらでも動作する想定。
RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu \
    "torch>=2.3,<3.0"

# アプリ依存
RUN pip install --no-cache-dir easyocr opencv-python matplotlib

# 作業ディレクトリ
WORKDIR /app

# プロジェクトファイルをコピー
COPY . .

# デフォルトコマンド
CMD ["python", "main.py"]
