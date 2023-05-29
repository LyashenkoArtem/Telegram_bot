FROM python:3.9-alpine

# Create a group and user
RUN addgroup -S dabot && adduser -S dabot -G dabot

RUN apk add tree

COPY --chown=dabot:dabot requirements.txt /dabot/
COPY --chown=dabot:dabot dist/Telegram_bot-v0.0.1.tar.gz /dabot/
RUN tar zvxf /dabot/Telegram_bot-v0.0.1.tar.gz -C /dabot/
RUN rm /dabot/Telegram_bot-v0.0.1.tar.gz

WORKDIR /dabot

RUN pip3 install -r requirements.txt

USER dabot

RUN tree /dabot

WORKDIR /dabot/Telegram_bot-v0.0.1/

CMD ["python3", "/dabot/Telegram_bot-v0.0.1/Da_Bot/Da_bot.py"]
