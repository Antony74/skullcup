FROM pymesh/pymesh

# Install nodejs 20.x
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

WORKDIR /root
COPY ./package.json /root/package.json
RUN npm install

