import subprocess


def install():

    try:
        import pip
    except ImportError:
        subprocess.call(
            [sys.executable, "-m", "pip", "install", "--user", "upgrade", "pip==9.0.3"]
        )

        import pip

    try:
        import numpy
    except ImportError:
        subprocess.call(["pip", "install", "numpy"])
    finally:
        import numpy

    try:
        from PIL import Image, ImageFile, ImageDraw
    except ImportError:
        subprocess.call(["pip", "install", "Pillow"])
    finally:
        from PIL import Image, ImageFile, ImageDraw


def output(fileName, img_li):
    install()
    import numpy
    from PIL import Image, ImageFile, ImageDraw

    array = numpy.array(img_li, dtype=numpy.uint8)

    img = Image.fromarray(array)
    img.save(fileName)


def euclidean(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
