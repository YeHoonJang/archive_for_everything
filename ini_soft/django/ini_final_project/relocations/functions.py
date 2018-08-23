def handle_uploaded_file(f):
    with open('../name.txt', 'wb+') as destination:
        for chunk in f.chunk():
            destination.write(chunk)