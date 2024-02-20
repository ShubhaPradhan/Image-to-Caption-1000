from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
karpathy_json_path='C:/Image-to-Caption-100/dataset_flickr8k.json',
image_folder='C:/Image-to-Caption-100/Flicker8k_Dataset',
captions_per_image=5,
min_word_freq=5,
output_folder='C:/Image-to-Caption-100/Flickr8k_preprocessed',
max_len=50)
