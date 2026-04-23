import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = {
  "spotify": "https://cdn.worldvectorlogo.com/logos/spotify-2.svg",
  "apple": "https://cdn.worldvectorlogo.com/logos/apple-music.svg",
  "youtube": "https://cdn.worldvectorlogo.com/logos/youtube-music-1.svg",
  "amazon": "https://cdn.worldvectorlogo.com/logos/amazon-music-1.svg"
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, context=ctx)
        data = response.read().decode('utf-8')
        print(f"SUCCESS: {name} (Length: {len(data)})")
        with open(f"{name}_test.svg", "w") as f:
            f.write(data)
    except Exception as e:
        print(f"FAILED: {name} - {e}")
