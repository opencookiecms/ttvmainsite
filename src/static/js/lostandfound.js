$(document).ready(function () {
   var links = document.querySelectorAll('.kil a')

   for (var i = 0; i < links.length; i++){
     var href =links[i].href
     var httpss = links[i].href
     if(href){
        links[i].href=href.replace('http://','https://');
       
     }
     if(httpss){
        links[i].href=href.replace(/localhost:8000/, encodeURIComponent("www.bursamalaysia.com"));
     }
     
   }

});
