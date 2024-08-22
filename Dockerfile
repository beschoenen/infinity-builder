FROM mobiledevops/android-sdk-image:34.0.0-jdk17

USER root

COPY . .

RUN apt-get update && \
    apt-get install -y git python3 wget

ENTRYPOINT ["/bin/sh"]
CMD ["./entrypoint.sh"]
