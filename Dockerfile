# Utilizza un'immagine base ufficiale di Python
FROM python:3.12-slim

# Imposta la directory di lavoro nel container
WORKDIR /scr

# Copia il file requirements.txt nel container
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto dei file dell'applicazione nel container
COPY . .



# Comando per eseguire l'applicazione
CMD ["python", "app.py"]
