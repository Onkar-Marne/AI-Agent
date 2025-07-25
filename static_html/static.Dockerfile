# Declare what image to use
# FROM user_name/image_name:latest (codingentrepreneurs/cfe_nginx:latest)
# FROM image_name:latest
FROM python:alpine3.22

WORKDIR /app

# RUN mkdir -p /staticfolder
# COPY ./static_html /staticfolder

# COPY ./static_html . (same meaning as the below command since destination is same)
COPY ./src .

# RUN echo "hello" > index.html


# docker build -f Dockerfile -t pyapp . (In terminal)
# docker run -it pyapp (In terminal)

# docker build -f Dockerfile -t onkar21298/ai-pyapp-test:latest . (In terminal)
# docker push onkar21298/ai-pyapp-test:latest (In terminal)

# python -m http.server 8000
# docker run -it -p 8000:8000 pyapp (In terminal)
CMD ["python", "-m", "http.server", "8000"]