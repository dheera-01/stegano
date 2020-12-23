from PIL import Image

#defining funtions

def change(lst): 			#changing 0-->1 and 1-->0 for more security
	for indx in range(len(lst)):
		if lst[indx]==1:
			lst[indx]=0
		else:
			lst[indx]=1


def store(lst,img): 		#storing 0's and 1's in R of each pixel
	global len_text_lst
	w,h = img.size
	px_itr = img.load()
	flag=0
	for j in range(h):
		for i in range(w):
			px_lst=list(px_itr[i,j])
			if lst[flag]==0 and px_lst[0]%2!=0:
				px_lst[0]+=1
			elif lst[flag]==1 and px_lst[0]%2==0:
				px_lst[0]+=1	
			px_tuple = tuple(px_lst)
			px_itr[i,j] = px_tuple
			flag+=1	
			if flag==len(lst):
				break
		if flag==len(lst):
			break
	for i in range(w):   	#storing len of text in last line of image and at last in row
		px_lst2 = list(px_itr[w-1-i,h-1])
		if i<len(len_text_lst):
			if len_text_lst[len(len_text_lst)-i-1]==0 and px_lst2[0]%2!=0:
				px_lst2[0]+=1
			elif len_text_lst[len(len_text_lst)-i-1]==1 and px_lst2[0]%2==0:
				px_lst2[0]+=1	
			px_tuple = tuple(px_lst2)
			px_itr[w-i-1,h-1] = px_tuple
		else:
			if px_lst2[0]%2!=0:
				px_lst2[0]+=1	
			px_tuple2 = tuple(px_lst2)
			px_itr[w-1-i,h-1] = px_tuple2
	img.save('secret.png')
	

def find_len(img):			#function which finds the len of text_lst from image
	w,h = img.size
	px_itr = img.load()
	len_str = ''
	for i in range(w):
		len_str += bin(px_itr[i,h-1][0])[-1]
	return int(len_str,2)*8  #returns a number representing number of pixels to be read


def extract(img):			 #extracting stored 0's and 1's as a list
	w,h = img.size
	px_itr = img.load()
	flag1 = find_len(img)
	flag2 = 0
	lst = []
	for j in range(h):
		for i in range(w):
			val = int(bin(px_itr[i,j][0])[-1])
			lst.append(val)
			flag2+=1
			if flag2==flag1:
				break
		if flag2==flag1:
			break
	return lst

	
def bintostr(lst):			#funtion for converting binary sequence into ascii text
	text_bin = ''
	text_final = ''
	for i in range(0,len(lst),8):
		for j in range(8):
			if i+7<len(lst): #barrier for avoinding out of index error
				text_bin+=str(lst[i+j])
		text_final+=chr(int(text_bin,2))
		text_bin=''
	return text_final
			

#program begins

print('STEGANOGRAPHY')		
print('CHOOSE THE TASK')
print('1. STORE MESSAGE')
print('2. EXTRACT MESSAGE')	
task = input('ENTER TASK NUMBER >>> ')

if task=='1':
	print('STORE MESSAGE INITIALIZING...')
	img_name = input('ENTER NAME OF IMAGE FILE WITH EXTENSION >>> ')
	img = Image.open(img_name)
	text = input('ENTER YOUR MESSAGE HERE >>> ').strip()
	
	len_text = len(text)
	len_text_lst = [int(b) for b in bin(len_text)[2:]]
	
	text_lst = []
	for char in text:
		bin_value = bin(ord(char))[2:]
		text_lst=text_lst+[int(b) for b in bin_value.zfill(8)]
	change(text_lst)
	store(text_lst,img)
	print('IMAGE SAVED AS secret.png')
	quit()

if task=='2':
	print('EXTRACT MESSAGE INITIALIZING...')
	img_name = input('ENTER NAME OF IMAGE FILE _____.png WITH EXTENSION >>> ')
	img = Image.open(img_name)
	message_lst = extract(img)
	change(message_lst)
	print('MESSAGE EXTRACTED!')
	print()
	print(bintostr(message_lst))
	print()
	print('MESSAGE EXTRACTED!')
	quit()
	
else:
	print('INVALID TASK NUMBER')
	quit()			
			
			

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		
		
