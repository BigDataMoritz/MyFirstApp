#Verwenden eines Basis Image 
From python:3.10 

#Definition des Arbeitsverzeichnisses
WORKDIR /app

#Kopieren des Codes 
COPY . /app 

#Installieren der Abhängigkeitn
RUN pip install -r requirements.txt 

# Verfügbarkeit des Ports 
EXPOSE 8501

#Start Applikation 
CMD ["streamlit", "run" , "app.py"]


