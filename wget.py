import requests, sys
from rich.progress import Progress
from rich import print
with Progress() as progress:
    url = sys.argv[1]
    chunk_size = 512
    connection = requests.get(url, stream=True)
    length = int(connection.headers['Content-Length'])
    print(f'File size: [blue]{length}[/blue] B')
    download = progress.add_task('[blue]Downloading ...', total=length / chunk_size)
    connection.raise_for_status()
    with open(url.split('/')[-1], 'wb') as file:
        for chunk in connection.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
            progress.update(download, advance=1)
     
