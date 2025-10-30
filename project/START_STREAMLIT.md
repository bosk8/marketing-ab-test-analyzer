# Starting the Streamlit App for Testing

Port 5503 is currently being used by a file server (directory listing). To test the Streamlit app, you need to start it on a different port or stop the file server.

## Option 1: Start Streamlit on Default Port (8501)

```bash
cd project
streamlit run app/ab_app.py
```

Then access: http://127.0.0.1:8501

## Option 2: Start Streamlit on Port 5503 (requires stopping file server first)

```bash
# Stop the file server on port 5503 first
cd project
streamlit run app/ab_app.py --server.port 5503
```

Then access: http://127.0.0.1:5503

## Option 3: Create Virtual Environment First

```bash
cd project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r config/requirements.txt
streamlit run app/ab_app.py
```

