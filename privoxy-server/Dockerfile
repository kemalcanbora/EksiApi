FROM alpine:3.10
LABEL maintainer="kemalcanbora@gmail.com"
LABEL description="Tor privoxy server"

RUN apk update && apk add privoxy
COPY config /etc/privoxy

EXPOSE 8118

ENTRYPOINT ["/usr/sbin/privoxy","--no-daemon","/etc/privoxy/config"]