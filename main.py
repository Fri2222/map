from functions import  get_location_x_y, path, html_path, openHtml
def main(start_location, end_location, start_point, approach_point, end_point):
	path_data=path(start_location,end_location)
	html_path(path_data,start_point,approach_point,end_point)
	openHtml()
if __name__ == '__main__':
	start_point = ("109.015868","34.290179")
	end_point = ("108.919276","34.273832")
	start_location = "109.015868,34.290179"
	end_location = "108.919276,34.273832"
	approach_point = ([108.919276,34.273832],[108.919276,34.273832],[109.015868,34.290179],[109.015868,34.290179])
	all_point = ([(109.015868,34.290179)],[108.919276,34.273832],[108.919276,34.273832],[109.015868,34.290179],[109.015868,34.290179],[108.919276,34.273832])
	main(start_location, end_location, start_point, approach_point, end_point)