# tts-server
docker run -it --rm \
    --name my-audio-container \
    --network host \
    --device /dev/snd \
    -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
    -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
    -u myuser \
    -v "$(pwd)/sample.wav:/sample.wav" \
    image-name
