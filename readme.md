1) create env
2) pip install req.txt
3) create ".env": 

""" ENV EXAMPLE """
ENV_NAME="Development"
BASE_URL="http://127.0.0.1:8000"
DB_URL="sqlite:///./shortener.db"

4)  uvicorn shortener_app.main:app --reload 
5) unbelievable! you are amazing! it works! 

