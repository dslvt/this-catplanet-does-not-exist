import numpy as np
from mayavi import mlab
import os
from tvtk.api import tvtk
import math
import matplotlib.pyplot as plt  # only for manipulating the input image
import subprocess

out_path = './'
out_path = os.path.abspath(out_path)
fps = 20
prefix = 'ani'
ext = '.png'

#TODO: use FLAGS to input data
def manual_sphere(image_file):
    # caveat 1: flip the input image along its first axis
    img = plt.imread(image_file)  # shape (N,M,3), flip along first dim
    outfile = image_file.replace('.jpg', '_flipped.jpg')
    # flip output along first dim to get right chirality of the mapping
    img = img[::-1, ...]
    plt.imsave(outfile, img)
    image_file = outfile  # work with the flipped file from now on

    # parameters for the sphere
    R = 2  # radius of the sphere
    Nrad = 180  # points along theta and phi
    phi = np.linspace(0, 2 * np.pi, Nrad)  # shape (Nrad,)
    theta = np.linspace(0, np.pi, Nrad)    # shape (Nrad,)
    phigrid, thetagrid = np.meshgrid(phi, theta)  # shapes (Nrad, Nrad)

    # compute actual points on the sphere
    x = R * np.sin(thetagrid) * np.cos(phigrid)
    y = R * np.sin(thetagrid) * np.sin(phigrid)
    z = R * np.cos(thetagrid)

    # create figure
    f = mlab.figure(size=(500, 500), bgcolor=(1, 1, 1))
    # f.scene.movie_maker.record = True

    # create meshed sphere
    mesh = mlab.mesh(x, y, z)
    mesh.actor.actor.mapper.scalar_visibility = False
    mesh.actor.enable_texture = True  # probably redundant assigning the texture later

    # load the (flipped) image for texturing
    img = tvtk.JPEGReader(file_name=image_file)
    texture = tvtk.Texture(
        input_connection=img.output_port, interpolate=1, repeat=0)
    mesh.actor.actor.texture = texture

    # tell mayavi that the mapping from points to pixels happens via a sphere
    # map is already given for a spherical mapping
    mesh.actor.tcoord_generator_mode = 'sphere'
    cylinder_mapper = mesh.actor.tcoord_generator
    # caveat 2: if prevent_seam is 1 (default), half the image is used to map half the sphere
    # use 360 degrees, might cause seam but no fake data
    cylinder_mapper.prevent_seam = 0
    # mlab.view(180.0, 90.0, 17.269256680431845, [0.00010503, 0.00011263, 0.])
    mlab.view(180.0, 90.0, 10, [0.00010503, 0.00011263, 0.])

    n_images = 36

    padding = len(str(n_images))
    mlab.roll(90.0)

    @ mlab.animate(delay=10, ui=False)
    def anim():
        for i in range(n_images):
            mesh.actor.actor.rotate_z(360 / n_images)

            zeros = '0'*(padding - len(str(i)))
            filename = os.path.join(
                out_path, '{}_{}{}{}'.format(prefix, zeros, i, ext))
            mlab.savefig(filename=filename)
            yield
        mlab.close(all=True)

    # cylinder_mapper.center = np.array([0,0,0])  # set non-trivial center for the mapping sphere if necessary
    # print(mlab.move())
    a = anim()
    mlab.show()

    ffmpeg_fname = os.path.join(
        out_path, '{}_%0{}d{}'.format(prefix, padding, ext))
    cmd = 'ffmpeg -f image2 -r {} -i {} -vcodec mpeg4 -y {}.mp4'.format(fps,
                                                                        ffmpeg_fname,
                                                                        prefix)
    subprocess.check_output(['bash', '-c', cmd])
    [os.remove(f) for f in os.listdir(out_path) if f.endswith(ext)]


manual_sphere('./image_smooth.jpg')
