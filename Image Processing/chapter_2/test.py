import os

def get_image_files(directory):
    image_files = []
    for root, directories, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif', 'bmp')):
                image_files.append(os.path.join(root, file))
    return image_files

# 가져올 이미지 파일이 있는 디렉토리 경로를 지정합니다.
directory_path = 'C:/'
image_files = get_image_files(directory_path)

print(len(image_files))

# 가져온 이미지 파일들을 출력합니다.
# for image_file in image_files:
#     print(image_file)
