FROM debian:latest
RUN useradd -m -u 1000 myuser

RUN apt-get update && apt-get install -y pulseaudio alsa-utils
# Set the user and group for PulseAudio
USER myuser:myuser

