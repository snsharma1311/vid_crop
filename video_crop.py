"""
Filename: video_crop.py
Usage: Takes video as an input argument display video frames to select region of interest, crops ROI and save video file in to destination path
Author: Shashank Sharma
"""
import cv2
import image_crop as ic
import sys

"""
takes videofile as a input
plays video, if paused opens a new window to select ROI, after selection auto plays
return diagonal points of ROI
"""
def select_ROI_video(filepath):
	try:
		cap = cv2.VideoCapture(filepath)
	except Exception as e:
		print str(e)
		sys.exit(1)

	window_name="press 'p' for pause, press 'q' after done"
	rect = [(0,0), (0,0)] #diagonal points
	#pause = False #flag to check play pause
		
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret:
			cv2.imshow(window_name, frame)
		else:
			break
		key = cv2.waitKey(30)	
		if key & 0xFF == ord('q'):
            		break
		if key & 0xFF == ord('p'):
			rect = ic.draw_rectangle(frame)
	cap.release()
	cv2.destroyAllWindows()
	return rect	

"""
takes src path, des path and diagonal points
rect[0]: top left
rect[1]: bottom right
saves cropped video as an AVI file, you can change codecs for other file formats check opencv docs
"""            		
def crop_and_save_video(src_path, des_path, rect):
	is_ROI_selected = (rect[0] != rect[1]) #true is diagonal points are not same	
	try:
		cap = cv2.VideoCapture(src_path)
	except Exception as e:
		print str(e)
		sys.exit(1)

	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	fps = 20
	width = rect[1][0] - rect[0][0]
	height = rect[1][1] - rect[0][1]
	out = cv2.VideoWriter(des_path, fourcc, fps, (width,height))
	while(cap.isOpened()):
    		ret, frame = cap.read()
		if ret==True:
			if not is_ROI_selected:
				out.write(frame)
			else:
				out.write(ic.crop_image(frame, rect))
		else:
			break
	cap.release()
	out.release()

"""
main runs as an example
"""
if __name__ == '__main__':
	rect = select_ROI_video('videos/test_video.mp4')
	crop_and_save_video('videos/test_video.mp4', 'videos/cropped.avi', rect)
	


