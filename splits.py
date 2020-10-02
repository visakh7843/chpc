import skimage
import skimage.io as skio
import random

class imageop:
	def open_image(self):
		self.img=skio.imread("out.jpg",False,None)
		self.imgA=[]
		self.imgB=[]
		h,w=self.img.shape
		for i in range(0,h):
			p=random.randint(1,random.randint(1,9))
			imgo=self.img[i]
			imga=[]
			imgb=[]
			for j in range(0,w):
				if(j%p==0):
					imga.append(imgo[j])
					imgb.append([0])
				else:
					imgb.append(imgo[j])
					imga.append([0])
			self.imgA.append(imga)
			self.imgB.append(imgb)
		self.imgAA=[]
		self.imgBB=[]
		for i in range(0,h):
			if(i%2==0):
				self.imgAA.append(self.imgA[i])
				self.imgBB.append(self.imgB[i])
			else:
				self.imgAA.append(self.imgB[i])
				self.imgBB.append(self.imgA[i])
		skio.imsave("out1.jpg",self.imgAA)
		skio.imsave("out2.jpg",self.imgBB)
		self.img2=[]
		for i in range(0,w):
			imgo=[]
			imga=self.imgAA[i]
			imgb=self.imgBB[i]
			for j in range(0,h):
				if(imga[j]==0):
					imgo.append(imgb[j])
				else:
					imgo.append(imga[j])
			self.img2.append(imgo)
		skio.imsave("out3.jpg",self.img2)

if __name__ == '__main__':
	name1=imageop()
	name1.open_image()
