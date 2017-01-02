import skimage
import skimage.io as skio

class imageop:
	def open_image(self):
		img=skio.imread("image.png",True,None)
		skio.imshow(img)

if __name__ == '__main__':
	name1=imageop()
	name1.open_image()
