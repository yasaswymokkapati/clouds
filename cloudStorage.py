import dropbox;
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
   # access_token = 'sl.Ak8BH81AX2WIptkkGu6ZPhQqtG4v0wK9dicMly-sUOSJiVl6UPP0SRc8j48IltYpz6w4DF1R7TzcFrBisdnB6RdIHoU8XVBW6e4SaSfMyhqzJRDOZUthe5SV8KZysOxf9rdQfbI'
    access_token = 'sl.Ak8S50lwER3LKvkGBAYQQaERqqn88d9WGgvrBsV7hbRYdndjwGhA81TdQT3PJJNPpuMspQlCmeJyAGfzHZuXWyg9NlWWo2ZxJ-w0tUZ6JGXO5J01MCAfeNwzJUFrnNoXDOcSbpYNDWI'
    transferData = TransferData(access_token)
    file_from = 'text.txt'
    file_to = '/test_dropbox/text.txt'
    transferData.upload_file(file_from, file_to)
    print('File has been moved')

main()