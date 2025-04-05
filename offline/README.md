# Slider Offline
- - -
### Instructions

These instructions are for setting up Slider Offline on a Raspberry Pi or similar Debian/Ubuntu.

1. Install Docker and Chromium
2. Install unclutter
    - This is optional, it is used to hide the mouse cursor
3. copy slider.service to /etc/systemd/system
4. Run `sudo systemctl enable slider.service`
5. Run `sudo systemctl start slider.service`
   - Run `sudo systemctl status slider.service` to check if the service is running
   - Run `sudo systemctl restart slider.service` to restart the service
6. Add pictures to /pictures
7. Slider will start automatically on boot and show all pictures in the /pictures folder