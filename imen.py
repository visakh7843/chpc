import skimage
import skimage.io as skio
import sys
import pickle

class imageops:
	def enc_image(self,inputim,outputim,passw):
		img2=skio.imread(inputim,False,None)
		img=skimage.img_as_ubyte(img2,force_copy=False)

		h,w,ch=img.shape
		passwords=list(passw)
		lists=[]
		for i in range(0,h):
			imgarr2=img[i]
			ptr2=0
			for j in range(0,w):
				imgarr=imgarr2[j]
				#ptr1=0
				for k in imgarr:
					valp=ord(passwords[ptr2])%256
					ptr2=ptr2+1
					if (ptr2>=len(passwords)):
						ptr2=0
					unit=int(chr(k).encode('hex'),16)
					enc=(unit+valp)%256
					lists.append(enc)
					#imgarr[ptr1]=enc#("%0.2X"%enc).decode('hex')
					#ptr1=ptr1+1
		lists.append(h)
		lists.append(w)
		lists.append(ch)
		print h,w,ch
		with open(outputim,'wb') as files:
			pickle.dump(lists,files)

	def dec_image(self,inputim,outputim,passw):
		with open (inputim,'rb') as files:
			imgl=pickle.load(files)
		size=imgl[-3:]
		print size
		img=[]
		ptr=0
		for i in range (0,size[0]):
			imgrow=[]
			for j in range(0,size[1]):
				imgpix=[]
				for k in range(0,size[2]):
					imgpix.append(imgl[ptr])
					ptr=ptr+1
				imgrow.append(imgpix)
			img.append(imgrow)
		print "\n\n"
		print img
		passwords=list(passw)
		for i in range(0,size[0]):
			imgarr2=img[i]
			ptr2=0
			for j in range(0,size[1]):
				imgarr=imgarr2[j]
				ptr1=0
				for k in imgarr:
					valp=ord(passwords[ptr2])%256
					ptr2=ptr2+1
					if (ptr2>=len(passwords)):
						ptr2=0
					#unit=int(k.encode('hex'),16)
					enc=(k-valp)%256#(unit-valp)%256
					imgarr[ptr1]=enc           #("%0.2X"%enc).decode('hex')
					ptr1=ptr1+1
		skio.imsave(outputim,img)

if __name__ == '__main__':
	name1=imageops()
	name1.enc_image("fisat.jpg","encoded.jpg","passw1234")
	name1.dec_image("encoded.jpg","decoded.jpg","passw1234")
