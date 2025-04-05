# Slider Offline
- - -
### Instructions

These instructions are for setting up Slider Offline on a Raspberry Pi or similar Debian/Ubuntu.

After some testing, I've found out that you need a Raspberry Pi 5 or similar to run the slider with Chromium. Old raspberries are not powerful enough to run Chromium and the slider at the same time. Allthough you might get lucky on lower resolutions.

1. Install Docker and Chromium
2. Install unclutter
    - This is optional, it is used to hide the mouse cursor. But you need to comment out the line in slider.service if you don't want to use it.
3. Copy slider.service to /etc/systemd/system
   - If not running as the first user, change the user value in the slider.service file
4. Run `sudo systemctl enable slider.service`
5. Run `sudo systemctl start slider.service`
   - Run `sudo systemctl status slider.service` to check if the service is running
   - Run `sudo systemctl restart slider.service` to restart the service
6. Make slider.sh executable: `sudo chmod +x slider.sh`
7. Add pictures to /pictures
8. Start slider container: `docker compose up -d`
9. Done! Slider will start automatically on boot and show all pictures in the /pictures folder in alphabetical order