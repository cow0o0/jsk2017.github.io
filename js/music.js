function playPause(params) {
    var music = document.getElementById("music");
    var aTitle = document.getElementById("aTitle");
    if(music.paused){
        music.play();
        aTitle.title="暂停音乐";
    }else{
        music.pause();
        aTitle.title="播放音乐";
    }
    
}