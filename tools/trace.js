const path = require('path'), fs = require('fs');
const potrace = require(path.join(process.argv[4], 'node_modules/potrace'));
const inDir = process.argv[2], outDir = process.argv[3];
fs.mkdirSync(outDir, {recursive: true});
const meta = JSON.parse(fs.readFileSync(path.join(inDir, 'meta.json')));
const keys = Object.keys(meta);
(async () => {
  for (const k of keys) {
    await new Promise((res, rej) => {
      const t = new potrace.Potrace({threshold: 128, turdSize: 12, optTolerance: 0.4, alphaMax: 1.0});
      t.loadImage(path.join(inDir, k + '.png'), err => {
        if (err) return rej(err);
        const tag = t.getPathTag();
        const d = (tag.match(/ d="([^"]+)"/) || [])[1];
        const subs = d.split(/(?=M)/).map(s => s.trim()).filter(Boolean);
        fs.writeFileSync(path.join(outDir, k + '.json'), JSON.stringify({w: meta[k].w, h: meta[k].h, paths: subs}));
        console.log(k, 'subpaths', subs.length, 'chars', d.length);
        res();
      });
    });
  }
})();
