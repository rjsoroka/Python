import webbrowser  

urls = [
    "https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/edit",
    "https://docs.python.org/3/library/functions.html#iter",
    "https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_",
    "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0XUsuxWHRQd"
]

def opener():
        webbrowser.open_new(urls[0])
        for url in urls:
            webbrowser.open(url, new=2)

opener()