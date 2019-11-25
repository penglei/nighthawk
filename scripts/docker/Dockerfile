FROM debian:bullseye-slim

RUN apt update -y && apt install curl iputils-ping dnsutils iproute2 procps telnet -y

COPY nighthawk_client /usr/local/bin

CMD ["/bin/bash"]
