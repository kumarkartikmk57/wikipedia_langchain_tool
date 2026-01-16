FROM python:3.10-slim
RUN apt-get update && apt-get install -y curl ca-certificates zstd && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://ollama.com/install.sh | sh
ENV OLLAMA_HOST=127.0.0.1:11434
ENV USER_AGENT=wiki/0.1
WORKDIR /app
COPY wiki.py /app
COPY fastapi_app.py /app
COPY streamlit_app.py /app
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir langchain-core langchain-ollama langchain-community langchain-postgres "psycopg[binary]" pypdf beautifulsoup4 requests httpx ollama fastapi uvicorn streamlit wikipedia
EXPOSE 11434
EXPOSE 8000
EXPOSE 8501
CMD ["sh","-lc","ollama serve & until curl -s http://127.0.0.1:11434/api/tags >/dev/null; do sleep 0.5; done; ollama pull ministral-3:3b && ollama pull nomic-embed-text:v1.5 && uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port 8501"]
