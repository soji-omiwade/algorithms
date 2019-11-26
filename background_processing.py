"""
the zipped file should have smaller size after it has been 
zipped.
"""
import threading
import zipfile
import unittest

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile): 
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        print("start ZipFile constructor ...")
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        print("start zip writing...")
        f.write(self.infile)
        print("done")
        f.close()
        print("returning")
        
def go(infile):
    async_zip = AsyncZip(infile, "b")
    async_zip.start()
    print('main continues, and will have to wait for background')
    async_zip.join()
    print('background is done')
    return open("b", "rb")
    
class TestCase(unittest.TestCase):
    def test_size_is_smaller(self):
        g = go("a.tar")
        bar = g.seek(0,2)
        f = open("a.tar","rb")
        self.assertGreaterEqual(f.seek(0,2), bar)
        f.close()
unittest.main()
        