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
		param[5] = True
	if event == cv2.EVENT_MOUSEMOVE:
		if param[5]:
			cv2.rectangle(img, param[3], (x, y), param[1])
	if event == cv2.EVENT_LBUTTONUP:
		param[4] = (x, y)
		cv2.rectangle(img, param[3], param[4], param[1])
		param[5] = False
	if param[5]:
		cv2.imshow(param[2],img)

"""
draw rectangle on to input frame/image
frame: input image
press 'q' to quit
"""
def draw_rectangle(frame):
	window_name = "press 'q' after done"
	cv2.namedWindow(window_name)
	color = (0, 0, 0) #black
	start_point = (0, 0) #(xs, ys)
	end_point = (0, 0) #(xe, ye)
	is_down = False #flag to check if left button was pressed before mouse move
	param = [frame, color, window_name, start_point, end_point, is_down]
	cv2.setMouseCallback(window_name, mouse_callback, param)
	cv2.imshow(window_name, frame)
	while True:
		if cv2.waitKey(1) & 0xFF == ord("q"):
        		break
	cv2.rectangle(frame, param[3], param[4], param[1])
	cv2.imshow('final', frame)
	cv2.waitKey(0)

if __name__ == '__main__':
	try:
		frame = cv2.imread('images/example_01.jpg')
	except Exception as e:
		print str(e)
	draw_rectangle(frame)

