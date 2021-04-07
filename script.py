from PIL import Image, ImageFilter
import face_recognition
import glob

files = glob.glob('**/*.jpg', recursive=True)
for file in files:
    if "_cropped" in file:
        print(f"Found photo: {file}")
        image = face_recognition.load_image_file(file)
        landmarks = face_recognition.face_landmarks(image)
        lm = landmarks[0]
        l_eye_dif = int((lm['left_eye'][4][1] + lm['left_eye'][5][1])/2 - (lm['left_eye'][1][1] + lm['left_eye'][2][1])/2)
        r_eye_dif = int((lm['right_eye'][4][1] + lm['right_eye'][5][1])/2 - (lm['right_eye'][1][1] + lm['right_eye'][2][1])/2)

        # ACOPERIRE OCHI STANG
        image = Image.open(file)
        cropped_image = image.crop((lm['left_eye'][0][0],lm['left_eye'][0][1]-l_eye_dif,lm['left_eye'][3][0],lm['left_eye'][3][1]+l_eye_dif))
        blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=25))
        image.paste(blurred_image, (lm['left_eye'][0][0],lm['left_eye'][0][1]-l_eye_dif,lm['left_eye'][3][0],lm['left_eye'][3][1]+l_eye_dif))
        # ACOPERIRE OCHI DREPT
        cropped_image = image.crop((lm['right_eye'][0][0],lm['right_eye'][0][1]-r_eye_dif,lm['right_eye'][3][0],lm['right_eye'][3][1]+r_eye_dif))
        blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=25))
        image.paste(blurred_image, (lm['right_eye'][0][0],lm['right_eye'][0][1]-r_eye_dif,lm['right_eye'][3][0],lm['right_eye'][3][1]+r_eye_dif))
        # SALVAM IMAGINEA
        image.save(file[:-4] + "_blurred.jpg")




