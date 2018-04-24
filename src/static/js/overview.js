function overviewHome(){
        var test = document.getElementById('search').value
        if(test == ''){
            //return window.location = ""
        }else{
            test = test.replace("#", "%23");
            window.location = "overview/" + test;
        }
}

function overview(){
        var test = document.getElementById('text').value
         if(test == ''){
            //return window.location = ""
        }else{
            test = test.replace("#", "%23");
            window.location = "/overview/" + test;
        }
}