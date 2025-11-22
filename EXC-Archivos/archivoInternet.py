import urllib.request

url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'


with urllib.request.urlopen(url) as response:
    contenido_bytes = response.read()
    contenido_texto = contenido_bytes.decode('utf-8')
    
print(contenido_texto)