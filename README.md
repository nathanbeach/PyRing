# Install
python3 -m pip install -r requirements.txt

# Notes for this hackage

run python pyring.py

if failures on individual downloads, retry by editing pyring.py line 104, call to cam_history

to concat the videos files, e.g.:

    printf "file '%s'\n" ./*.mp4 > files.txt
    ffmpeg -f concat -safe 0 -i files.txt -c copy ../2020_11_ring_cam.mp4
