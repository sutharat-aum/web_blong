function searchHome(){
        var test = document.getElementById('search').value
        if(test == ''){
            //return window.location = ""
        }else{
            test = test.replace("#", "%23");
            window.location = "search/" + test;
        }
}

function search(){
        var test = document.getElementById('text').value
         if(test == ''){
            //return window.location = ""
        }else{
            test = test.replace("#", "%23");
            window.location = "/search/" + test;
        }
}