FROM python:3.6
RUN pip install -i https://mirror.nju.edu.cn/pypi/web/simple fastapi
RUN pip install -i https://mirror.nju.edu.cn/pypi/web/simple psutil
RUN pip install -i https://mirror.nju.edu.cn/pypi/web/simple "uvicorn[standard]"

COPY main.py .
COPY tools.py .


EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
