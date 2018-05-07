import gzip

fn = 'gest.gz'
s = 'sdfas stromg asdf asdfas'
f = gzip.open(fn, mode='wt')
f.write(s)
f.close()