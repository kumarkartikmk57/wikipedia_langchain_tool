# wikipedia_langchain_tool

This application uses an LLM along with Wikipedia data to fetch, analyze, and generate detailed family information for well‑known celebrities.

---

## 🚀 How to Run the Application

You can run this application in two ways:

---

## 1. Prebuilt Docker Image

Use the ready‑to‑run image from Docker Hub:

```bash
docker pull kumarkartikmk57/wiki_family_tree:latest
docker run --gpus all -p 8501:8501 kumarkartikmk57/wiki_family_tree:latest
```
## 2. Build locally
Clone the repository and build the image manually:
```bash
git clone <repo-url>
cd <repo-folder>
docker build -t wiki_family_tree:latest .
docker run --gpus all -p 8501:8501 wiki_family_tree:latest

```
