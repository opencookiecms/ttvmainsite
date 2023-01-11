$(document).ready(function () {
   var links = document.querySelectorAll('.kil a')

   for (var i = 0; i < links.length; i++){
     var href =links[i].href
     var httpss = links[i].href
     if(href){
        links[i].href=href.replace('http://','https://');
       
     }
     if(httpss){
        links[i].href=href.replace(/ttvision-tech.com/, encodeURIComponent("bursamalaysia.com"));
     }
     
   }

});


$(document).ready(function () {
   var links = document.querySelectorAll('.lop a')
   for (var i = 0; i < links.length; i++){
     var href =links[i].href   
     var httpss = links[i].href
     if(href){
        links[i].href=href.replace('http://','https://');
        links[i].innerHTML = "More Info"
        links[i].className= "btn btn-primary"
      
       
     }
     if(httpss){
        links[i].href=href.replace(/ttvision-tech.com/, encodeURIComponent("bursamalaysia.com"));
     }
     
   }

});



$(document).ready(function () {
   var links = document.querySelectorAll('.tags a')
   
 

   for (var i = 0; i < links.length; i++){
     var href =links[i].href 
     var httpss = links[i].href
     if(href){
   
        links[i].href=href.replace('http://','https://');
       
     }
     if(httpss){
        links[i].href=href.replace(/ttvision-tech.com/, encodeURIComponent("bursamalaysia.com"));
     }
     
   }

});


