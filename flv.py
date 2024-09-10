from animeflv import AnimeFLV

with AnimeFLV() as api:
    elements = api.search(input("escribe serie de anime:"))
for i, element in enumerate(elements):
     print(f"{i},{element.title}")
try:
         selection = int(input("selecciona opcion:"))
         info = api.get_anime_info(elements[selection].id)
         info.episodes.reverse()
         for j, episode in enumerate(info.episodes):
             print(f"{j}|Episode-{episode.id}")
             index_episode = int(input("selecciona episodio:"))
             serie = elements[selection].id
             capitulo = info.episodes[index_episode].id
             results = api.get_links(serie, capitulo)
             for result in enumerate(results):
                 print(f"{result.url}") 
            
except Exception as e:
            print(e)
