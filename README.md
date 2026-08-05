sudo nano /etc/systemd/system/soundboard.service

[Unit]
Description=Pi Soundboard
After=sound.target

[Service]
Type=simple
User=loz
WorkingDirectory=/home/loz/soundboard
ExecStart=/usr/bin/python3 /home/loz/soundboard/soundboard.py
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target

#Add under [service] if audio does not play on autostart, either
#Environment=SDL_AUDIODRIVER=alsa
#Environment=XDG_RUNTIME_DIR=/run/user/1000

sudo systemctl daemon-reload
sudo systemctl enable soundboard.service
sudo systemctl start soundboard.service
sudo systemctl status soundboard.service

#If it shows failed, run
#journalctl -u soundboard.service -e

sudo reboot
