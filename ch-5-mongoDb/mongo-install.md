- I (Claude) will guide you through installing MongoDB on Manjaro Linux. Here are the steps:

1. First, update your system:

```bash
sudo pacman -Syu
```

2. MongoDB is available in the Arch User Repository (AUR). You'll need an AUR helper like `yay`. If you don't have yay installed:

```bash
sudo pacman -S yay
```

3. Install MongoDB using yay:

```bash
yay -S mongodb-bin
```

4. Install MongoDB tools (optional but recommended):

```bash
yay -S mongodb-tools-bin
```

5. Enable and start the MongoDB service:

```bash
sudo systemctl enable mongodb
sudo systemctl start mongodb
```

6. Verify the installation:

```bash
mongosh
```

If everything is working, you should see the MongoDB shell prompt. You can exit the shell by typing `exit`.

Common troubleshooting:

- If the service fails to start, check the logs: `sudo journalctl -u mongodb`
- Make sure you have sufficient permissions for the data directory
- If you encounter permission issues, you might need to create and set proper ownership for the data directory:

```bash
sudo mkdir -p /data/db
sudo chown -R mongodb:mongodb /data/db
```
