FROM alpine:edge
LABEL maintainer="kemalcanbora@gmail.com"
LABEL description="Tor server"

RUN apk update && apk add tor
COPY torrc.default /etc/tor

EXPOSE 9050 9051

ENTRYPOINT ["/usr/bin/tor","-f","/etc/tor/torrc.default"]