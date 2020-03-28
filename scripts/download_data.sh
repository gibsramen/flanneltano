youtube-dl \
    --skip-download \
    --write-thumbnail \
    --write-description \
    --write-info-json \
    --match-title 'album review' \
    -o \
    '../data/album_reviews/%(upload_date)s_%(title)s/%(upload_date)s_%(title)s.%(ext)s' \
    https://www.youtube.com/user/theneedledrop/videos
