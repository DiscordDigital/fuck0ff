import os, sys
from PIL import Image, ImageDraw, ImageOps

croptop = 200
cropleft = 0
cropbottom = 0
transparency = 80
lang = "en"

# Checking arguments
if len(sys.argv) == 1:
    print("Syntax: buildfuck.py awesome-wallpaper.jpg awesome")
    print("The result will be a theme file named awesome.zip")
    exit()
buildname = sys.argv[2]

# Calculating transparency to a value pillow understands
transparency = int((transparency/100) * 255)

# Clearing build folder
os.system("rm build/*")

# Checking template folder
if not os.path.exists('template'):
    print("template folder does not exist. Please run './fuck0ff.sh extract-template' first")
    exit()

if len(os.listdir('template') ) == 0:
    print("template folder is empty. Please run './fuck0ff.sh extract-template' first")
    exit()

# Resize to basewidth
basewidth = 839
img = Image.open(sys.argv[1])
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
width, height = img.size

left = cropleft
top = croptop
right = width
bottom = height - cropbottom

img = img.crop((left,top,right,bottom))

#img.save('wallpaper.thumbnail.jpeg') 

# Cropping process of backgrounds
# 3 per line
# start left and start top from 0
# 225 x 255 each block
objsize = 225
padding = 80
toppadding = 48

offsettop = 0
offsetleft = 0
offsetright = objsize
offsetbottom = objsize

size = (objsize, objsize)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=transparency)


n1 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n1 = ImageOps.fit(n1, mask.size, centering=(0.5, 0.5))
n1.putalpha(mask)
n1fg = Image.open("template/en-1---white.png")
n1.paste(n1fg, (0, 0), n1fg)
n1.save('build/' + lang + '-1---white.png')
n1.save('build/' + lang + '-1---mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n2 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n2 = ImageOps.fit(n2, mask.size, centering=(0.5, 0.5))
n2.putalpha(mask)
n2fg = Image.open("template/en-2-A B C--white.png")
n2.paste(n2fg, (0, 0), n2fg)
n2.save('build/' + lang + '-2-A B C--white.png')
n2.save('build/' + lang + '-2-A B C--mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n3 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n3 = ImageOps.fit(n3, mask.size, centering=(0.5, 0.5))
n3.putalpha(mask)
n3fg = Image.open("template/en-3-D E F--white.png")
n3.paste(n3fg, (0, 0), n3fg)
n3.save('build/' + lang + '-3-D E F--white.png')
n3.save('build/' + lang + '-3-D E F--mask.png')

offsetleft = 0
offsetright = objsize
offsettop = offsettop + objsize + toppadding
offsetbottom = offsetbottom + objsize + toppadding
n4 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n4 = ImageOps.fit(n4, mask.size, centering=(0.5, 0.5))
n4.putalpha(mask)
n4fg = Image.open("template/en-4-G H I--white.png")
n4.paste(n4fg, (0, 0), n4fg)
n4.save('build/' + lang + '-4-G H I--white.png')
n4.save('build/' + lang + '-4-G H I--mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n5 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n5 = ImageOps.fit(n5, mask.size, centering=(0.5, 0.5))
n5.putalpha(mask)
n5fg = Image.open("template/en-5-J K L--white.png")
n5.paste(n5fg, (0, 0), n5fg)
n5.save('build/' + lang + '-5-J K L--white.png')
n5.save('build/' + lang + '-5-J K L--mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n6 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n6 = ImageOps.fit(n6, mask.size, centering=(0.5, 0.5))
n6.putalpha(mask)
n6fg = Image.open("template/en-6-M N O--white.png")
n6.paste(n6fg, (0, 0), n6fg)
n6.save('build/' + lang + '-6-M N O--white.png')
n6.save('build/' + lang + '-6-M N O--mask.png')

offsettop = offsettop + objsize + toppadding
offsetbottom = offsetbottom + objsize + toppadding
offsetleft = 0
offsetright = objsize
n7 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n7 = ImageOps.fit(n7, mask.size, centering=(0.5, 0.5))
n7.putalpha(mask)
n7fg = Image.open("template/en-7-P Q R S--white.png")
n7.paste(n7fg, (0, 0), n7fg)
n7.save('build/' + lang + '-7-P Q R S--white.png')
n7.save('build/' + lang + '-7-P Q R S--mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n8 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n8 = ImageOps.fit(n8, mask.size, centering=(0.5, 0.5))
n8.putalpha(mask)
n8fg = Image.open("template/en-8-T U V--white.png")
n8.paste(n8fg, (0, 0), n8fg)
n8.save('build/' + lang + '-8-T U V--white.png')
n8.save('build/' + lang + '-8-T U V--mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n9 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n9 = ImageOps.fit(n9, mask.size, centering=(0.5, 0.5))
n9.putalpha(mask)
n9fg = Image.open("template/en-9-W X Y Z--white.png")
n9.paste(n9fg, (0, 0), n9fg)
n9.save('build/' + lang + '-9-W X Y Z--white.png')
n9.save('build/' + lang + '-9-W X Y Z--mask.png')

offsettop = offsettop + objsize + toppadding
offsetbottom = offsetbottom + objsize + toppadding
offsetleft = 0
offsetright = objsize
nStar = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
nStar = ImageOps.fit(nStar, mask.size, centering=(0.5, 0.5))
nStar.putalpha(mask)
nStarfg = Image.open("template/en-_---white.png")
nStar.paste(nStarfg, (0, 0), nStarfg)
nStar.save('build/' + lang + '-_---white.png')
nStar.save('build/' + lang + '-_---mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
n0 = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
n0 = ImageOps.fit(n0, mask.size, centering=(0.5, 0.5))
n0.putalpha(mask)
n0fg = Image.open("template/en-0-+--white.png")
n0.paste(n0fg, (0, 0), n0fg)
n0.save('build/' + lang + '-0-+--white.png')
n0.save('build/' + lang + '-0-+--mask.png')

offsetleft = offsetleft + objsize + padding
offsetright = offsetright + objsize + padding
nHash = img.crop((offsetleft,offsettop,offsetright,offsetbottom))
nHash = ImageOps.fit(nHash, mask.size, centering=(0.5, 0.5))
nHash.putalpha(mask)
nHashfg = Image.open("template/en-#---white.png")
nHash.paste(nHashfg, (0, 0), nHashfg)
nHash.save('build/' + lang + '-#---white.png')
nHash.save('build/' + lang + '-#---mask.png')
 
os.system("zip -r -j " + buildname + '.zip build/*')

print("Done!")
