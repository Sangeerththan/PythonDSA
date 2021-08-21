# pip3 install python-libtorrent-bin==1.2.12
# Reference: https://gist.github.com/samukasmk/940ca5d5abd9019e8b1af77c819e4ca9
import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/home/sangee/Torrents',
    'storage_mode': lt.storage_mode_t(2)}
link = "magnet:?xt=urn:btih:2614240fe0c1e58c7773d0ec3ec4505185339ed7&dn=www.1TamilMV.one%20-%20NETRIKANN%20(" \
       "2021)%20Tamil%20HQ%20HDRip%20-%20720p%20-%20x264%20-%20(" \
       "DD%2b5.1%20-%20192Kbps%20%26%20AAC)%20-%201.4GB%20-%20ESub.mkv&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337" \
       "%2fannounce&tr=http%3a%2f%2fpow7.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr" \
       "=http%3a%2f%2ftracker2.itzmx.com%3a6961%2fannounce&tr=udp%3a%2f%2f151.80.120.114%3a2710%2fannounce&tr=udp%3a" \
       "%2f%2f9.rarbg.com%3a2790%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2740%2fannounce&tr=udp%3a%2f%2fopen.stealth" \
       ".si%3a80%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker" \
       ".opentrackr.org%3a1337%2fannounce&tr=http%3a%2f%2ft.nyaatracker.com%3a80%2fannounce "
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

print('downloading metadata...')
while not handle.has_metadata():
    time.sleep(1)
print('got metadata, starting torrent download...')
while handle.status().state != lt.torrent_status.seeding:
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
                 'downloading', 'finished', 'seeding', 'allocating']
    print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
           s.num_peers, state_str[s.state]))
    time.sleep(5)
