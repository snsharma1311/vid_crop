import cv2

"""
mouse callback function.
param[0]: image
param[1]: color
param[2]: window_name
left click down: (xs, ys) starting point
mouse move: (x', y') intermediate points draw rectangle using (xs, ys, x', y')
left click up: (xe, ye) end points draw final rectangle
"""
def mouse_callback(event, x, y, flags, param):
	img = param[0].copy()
	if event == cv2.EVENT_LBUTTONDOWN:
		param[3] = (x, y)
		param[4] = True
	if event == cv2.EVENT_MOUSEMOVE:
		if param[4]:
			cv2.rectangle(img, param[3], (x, y), param[1])
	if event == cv2.EVENT_LBUTTONUP:
		cv2.rectangle(img, param[3], (x, y), param[1])
		param[3] = (0, 0)
		param[4] = False
	if param[4]:
		cv2.imshow(param[2],img)

"""
draw rectangle on to input frame/image
frame: input image
press 'z': to redraw
press 'q': to finalize
"""
def draw_rectangle(frame):
	ann_frame = frame.copy() #copy of image to be annotated
	window_name = "press 'z'to redraw and press 'q' after done"
	cv2.namedWindow(window_name)
	color = (0, 0, 0) #black
	start_point = (0, 0) #(xs, ys)
	is_down = False #flag to check if left button was pressed before mouse move
	param = [frame, color, window_name, start_point, is_down]
	cv2.setMouseCallback(window_name, mouse_callback, param)
	cv2.imshow(window_name, ann_frame)
	while True:
		if cv2.waitKey(1) & 0xFF == ord("q"):
        		break
		if cv2.waitKey(1) & 0xFF == ord("z"):
			ann_frame = frame.copy()
			cv2.imshow(window_name, ann_frame)

if __name__ == '__main__':
	try:
		frame = cv2.imread('images/example_01.jpg')
	except Exception as e:
		print str(e)
	draw_rectangle(frame)

