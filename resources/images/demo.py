from PIL import Image
import optparse
# import logging

# logger = logging.basicConfig(level=logging.DEBUG)
usage = 'Usage: %prog [-h-o-c1-c2-cc-p] arg1 arg2 ...'
parser = optparse.OptionParser(usage, version="%prog 1.0")
parser.add_option('-o', '--output', type=str,
                  action='store', dest='output', 
                  metavar="FILE", help='write output to FILE')
parser.add_option('-s', '--show',
                  action='store_true', dest='show',
                  help='show image attributes')
parser.add_option('--c1', '--pisel_one',
                  action='store_true', dest='pisel_one',
                  metavar='pisel(1024,768)',
                  help="change image pixel in (1024,768),old image's pisel must larger than new image")
parser.add_option('--c2', '--pisel_two',
                  action='store_true', dest='pisel_two',
                  metavar='pisel(1920,1280)',
                  help="change image pixel in (1920,1280),old image's pisel must larger than new image")
parser.add_option('--cc', '--pisel_xy', type=str,
                  action='store', dest='pisel_xy',
                  metavar='pisel(x,y)', help="change image pixel in (x,y),old image's pisel must larger than new image")


def storePicture(ins, out):
    try:
        lena = Image.open(ins)
        lena.save(out)
    except Exception as e:
        print '''can't open image "{}"'''.format(ins)


def change2pixel_one(ins, output):
    try:
        lena = Image.open(ins)
        old_size = lena.size
        lena.thumbnail((1024, 768))
        lena.save(output)
        print '''success change "{}{}" into "{}{}".'''.format(ins, old_size, output, lena.size)
    except Exception as e:
        print '''can't open image "{}"'''.format(ins)


def change2pixel_two(ins, output):
    try:
        lena = Image.open(ins)
        old_size = lena.size
        lena.thumbnail((1920, 1280))
        lena.save(output)
        print '''success change "{}{}" into "{}{}".'''.format(ins, old_size, output, lena.size)
    except Exception as e:
        print '''can't open image "{}"'''.format(ins)


def change2pixel_xy(ins, output, xy):
    try:
        lena = Image.open(ins)
        old_size = lena.size
        xy = xy.split(',')
        lena.thumbnail((int(xy[0]), int(xy[1])))
        lena.save(output)
        print '''success change "{}{}" into "{}{}".'''.format(ins, old_size, output, lena.size)
    except Exception as e:
        print e.message
        # print '''can't open image "{}"'''.format(ins)


def showAttribute(ins):
    try:
        lena = Image.open(ins)
        print "mode:{}\nsize:{}".format(lena.mode, lena.size)
    except Exception as e:
        print '''can't open image "{}"'''.format(ins)


(options, args) = parser.parse_args()
if not args:
    print 'please input you image!'
else:
    output=args[0]
    ins = args[0]
    if options.output:
        output = options.output
    if options.show:
        showAttribute(ins)
    if options.pisel_one:
        change2pixel_one(ins, output)
    if options.pisel_two:
        change2pixel_two(ins, output)
    if options.pisel_xy:
        xy = options.pisel_xy
        change2pixel_xy(ins, output, xy)
