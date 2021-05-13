FROM node:latest
 
COPY foundryvtt.tgz ./

RUN mkdir foundrydata && \
    tar -xzvf foundryvtt.tgz && \
    rm foundryvtt.tgz

CMD node foundryvtt/resources/app/main.js --dataPath=foundrydata --port=80
 
