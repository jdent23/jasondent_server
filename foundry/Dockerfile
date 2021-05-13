FROM node:latest
 
COPY foundryvtt.tgz ./

RUN mkdir foundrydata && \
    tar -xzvf foundryvtt.tgz && \
    rm foundryvtt.tgz

EXPOSE 80

CMD node foundryvtt/resources/app/main.js --dataPath=foundrydata
 
