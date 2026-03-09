FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    openssl \
    ruby \
    procps \
    vim-common \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN chmod +x /app/deploy/akash/entrypoint.sh \
    /app/launch_test_master_base_v8_6_fortress.sh \
    /app/launch_test_master_base_v8_5_impact.sh \
    /app/launch_test_duo_harmonic_5_8_13_6h.sh \
    /app/ACE777_STRICT_CLONE_FUTURES_V2.sh \
    /app/ACE777_STRICT_CLONE_FUTURES.sh

ENTRYPOINT ["/app/deploy/akash/entrypoint.sh"]
