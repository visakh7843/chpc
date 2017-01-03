import skimage
import skimage.io as skio

class imageop:
	def open_image(self):
		self.img=skio.imread("image.png",True,None)
		skio.imsave("out.jpg",self.img)
		print self.img.shape
		print self.img.size
		for i in range(0,512):
			for j in range(0,512):
				if self.img[i,j]<0.5:
					self.img[i,j]=0
				else:
					self.img[i,j]=1
		skio.imsave("out1.jpg",self.img)
if __name__ == '__main__':
	name1=imageop()
	name1.open_image()
