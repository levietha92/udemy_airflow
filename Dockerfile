FROM astrocrpublic.azurecr.io/runtime:3.0-3
# setting up SSH
# RUN apt-get update && apt-get install -y openssh-client && rm -rf /var/lib/apt/lists/*