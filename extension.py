#In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

def get_media_type(file_name: str) -> str:  
    if file_name.lower().endswith('.gif'):
        return 'image/gif'
    elif file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
        return 'image/jpeg'
    elif file_name.lower().endswith('.png'):
        return 'image/png'
    elif file_name.lower().endswith('.pdf'):
        return 'application/pdf'
    elif file_name.lower().endswith('.txt'):
        return 'text/plain'
    elif file_name.lower().endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'

def main():
    file_name = input("File name: ").strip()
    media_type = get_media_type(file_name)
    print(media_type)

main()