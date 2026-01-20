# 2. Download the actual binary for x86_64
curl -L -o ~/.docker/cli-plugins/docker-buildx \
"https://github.com/docker/buildx/releases/download/v0.30.1/buildx-v0.30.1.linux-amd64"

# 3. Make it executable again
chmod +x ~/.docker/cli-plugins/docker-buildx

# 4. Verify it actually works now
docker buildx version