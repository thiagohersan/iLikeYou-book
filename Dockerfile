FROM python:2.7-jessie

ENV BOOK_NAME iLikeYou

RUN apt-get update
RUN apt-get install -y libgif4

RUN mkdir -p /tmp/prince && mkdir -p /tmp/book && mkdir -p /opt/book

WORKDIR /tmp/prince/
RUN curl -Os https://www.princexml.com/download/prince_11.3-1_debian8.0_amd64.deb
RUN dpkg -i prince_11.3-1_debian8.0_amd64.deb && apt-get install -f

WORKDIR /tmp/book/
ADD *.html *.css *.py /tmp/book/
ADD imgs /tmp/book/imgs
ADD fonts /tmp/book/fonts
RUN python prepBook.py

RUN prince -s style.css ${BOOK_NAME}.html -o ${BOOK_NAME}.pdf

CMD cp ${BOOK_NAME}.pdf /opt/book/
