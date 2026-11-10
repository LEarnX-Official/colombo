import sys, os, json
from PIL import Image, ImageOps, ImageFilter
src = sys.argv[1]; out = sys.argv[2]
os.makedirs(out, exist_ok=True)
D = {
 'face-woman': '2022_10_Colombo-Logo-e-Disegni1.png',
 'doctor': '2022_10_Progetto-senza-titolo-22.png',
 'breast-pair': '2022_10_Colombo-Logo-e-Disegni-4-scaled.jpg',
 'eyes': '2022_10_Colombo-Logo-e-Disegni3.png',
 'profile-jaw': '2022_10_Schermata-2022-10-03-alle-15.39.04.png',
 'mastopexy': '2022_10_Schermata-2022-10-03-alle-19.43.27.png',
 'eye-brow': '2022_10_Schermata-2022-10-20-alle-15.24.19.png',
 'dash-arrow': '2022_10_Schermata-2022-10-03-alle-19.55.24.png',
 'lip-profile': '2022_10_Schermata-2022-10-03-alle-15.13.04.png',
 'ear-neck': '2022_10_Schermata-2022-10-03-alle-15.15.26.png',
 'molecule': '2022_10_Schermata-2022-10-03-alle-19.16.24.png',
 'male-torso': '2022_10_Schermata-2022-10-03-alle-19.41.10.png',
 'female-torso': '2022_10_Schermata-2022-10-03-alle-19.45.59.png',
 'implant': '2022_10_Schermata-2022-10-03-alle-19.48.32.png',
 'half-face': '2022_10_Schermata-2022-10-20-alle-17.53.43.png',
 'symbol': '2022_10_cropped-Favicon-colombo.png',
 'logo-script': '2022_10_cropped-Schermata-2022-10-03-alle-13.47.03.png',
}
meta = {}
for key, fn in D.items():
    im = Image.open(os.path.join(src, fn)).convert('RGBA')
    bg = Image.new('RGBA', im.size, (255,255,255,255)); bg.alpha_composite(im)
    g = bg.convert('L')
    W, H = g.size
    crop = key != 'doctor'
    scale = 1.0
    if crop:
        bw = g.point(lambda v: 255 if v < 215 else 0)
        bbox = bw.getbbox()
        m = int(max(W, H) * 0.02)
        bbox = (max(0,bbox[0]-m), max(0,bbox[1]-m), min(W,bbox[2]+m), min(H,bbox[3]+m))
        g = g.crop(bbox)
        target = 1600
        scale = target / max(g.size)
        if scale > 1.05:
            g = g.resize((round(g.size[0]*scale), round(g.size[1]*scale)), Image.LANCZOS)
            g = g.filter(ImageFilter.GaussianBlur(1.2))
        else:
            scale = 1.0
    b = g.point(lambda v: 0 if v < 200 else 255).convert('L')
    b.save(os.path.join(out, key + '.png'))
    meta[key] = {'w': b.size[0], 'h': b.size[1], 'src': fn, 'orig': [W, H], 'scale': scale}
    print(key, (W, H), '->', b.size)
json.dump(meta, open(os.path.join(out, 'meta.json'), 'w'), indent=1)
