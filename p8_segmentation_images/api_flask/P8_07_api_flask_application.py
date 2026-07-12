from flask import Flask, render_template, url_for, request
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import base64
import json
import pickle
import os


app = Flask(__name__)


@app.route('/')
def index():
	return ("Segmentation image : use api")


@app.route('/api/v1/segim/<string:id>', methods=['GET'])
def api_id(id):


	# resize image for network speed purposes
	resize_dims = (224,224)
	
	image_source_path, image_seg_path = get_images_path(id)

	image_source_array, source_dims = load_image_as_array(image_source_path, resize_dims)


	# send image to segmentation model
	serialized_img_as_json = serialize_img_as_json(image_source_array)
	resp = send_data_to_model(serialized_img_as_json)
	image_model_resp = deserialize_resp_from_json(resp)

	# restore original image dims
	image_model_resp = resize_image(image_model_resp, source_dims)

	# encode image for display
	im_encode = array_image_encode(image_model_resp)

	return render_template(
		'base.html',
		img_source=url_for('static', filename=image_source_path),
		img_seg=url_for('static', filename=image_seg_path),
		img_pred=im_encode,
		)


def send_data_to_model(data):
	headers = {"Content-Type": "application/json", 'Accept': 'text/plain'}
	request_url = 'http://fc947c4b-0da2-41a2-831c-e66cf24d43bb.centralus.azurecontainer.io/score'
	resp = requests.post(request_url, data, headers=headers)
	return resp

def serialize_img_as_json(img_array):
	serialized_as_json = json.dumps(pickle.dumps(img_array).decode('latin-1'))
	return serialized_as_json

def deserialize_resp_from_json(resp):
	deserialized_from_json = ''
	if resp.status_code == 200:
		deserialized_from_json = pickle.loads(json.loads(resp.json()).encode('latin-1'))
	return deserialized_from_json

def array_image_encode(seg_image):
	if seg_image == '':
		return ''
	im_pil = seg_image
	if im_pil.mode != 'RGB':
		im_pil = im_pil.convert('RGB')
	buff = BytesIO()
	im_pil.save(buff, format="png")
	im_b64 = ''
	im_b64 = base64.b64encode(buff.getvalue()).decode("utf-8")
	return im_b64

def load_image_as_array(image_path, resize_dims=None):

	image_array = ''
	source_dims = ''

	if image_path != '':
		image_loaded = Image.open('static/' + image_path).convert("RGB")
		image_array = np.array(image_loaded)
		source_dims = image_array.shape
		if resize_dims is not None:
			image_array = np.array(image_loaded.resize(resize_dims))

	return image_array, source_dims

def resize_image(image_to_resize, dims):
	if image_to_resize != '':
		image_to_resize = image_to_resize.resize((dims[1],dims[0]))
	return image_to_resize

        
def get_images_path(image_id):

	filepath = 'images/'
	images_list = os.listdir('static/' + filepath + 'image')
	masks_list = os.listdir('static/' + filepath + 'mask')

	source_name = ''
	mask_name = ''
	source_file = ''
	mask_file = ''
	id_town = 'wrong_id'
	id_num = 'wrong_id'

	id_split = image_id.split("_")
	if len(id_split) == 3:
		id_town = id_split[0]
		id_num = id_split[1].rjust(6,'0') + '_' + id_split[2].rjust(6,'0')	


	source_list = [x for x in images_list if id_num in x and x.startswith(id_town)]
	mask_list = [x for x in masks_list if id_num in x and x.startswith(id_town)]

	if len(source_list)>0:
		source_name = source_list[0]
		mask_name = mask_list[0]
		source_file = filepath + 'image/' + source_name 
		mask_file = filepath + 'mask/' + mask_name 

	return source_file, mask_file


if __name__ == '__main__':

   app.run()