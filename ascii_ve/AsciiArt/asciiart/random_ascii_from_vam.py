from ascii_ve.AsciiArt.asciiart import asciify
from ascii_ve.AsciiArt.asciiart import vam
#Get random image

print("Fetching a radom image from the V&A collection...")
filename = vam.download_random_vam_image()
print('done', 'saved as '+ filename)
asciify.ascii(filename)

