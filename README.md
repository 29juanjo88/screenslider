jquery_screenslider
===================

This jquery plugin allows you to make a slideshow in the background of your website
Resize your browser to see the resposive behavior

How to use:
------------

Html: Make the structure of your html file to be similar to this:

          <!-- Include jQuery -->
          <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
          
          <!-- Just include this 2 files -->
          <link rel="stylesheet" href="screenslider/css/screenslider.css">
          <script src="screenslider/js/screenslider.js"></script>
          
          <!-- And your regular js file -->
          <script src="js/main.js"></script>


          <!-- Make your page structure to be similar to the following -->
          <div id="screenslider">
          <!-- Include 1 image for each slide -->
            <img src="slide2.jpg" />
            <img src="slide1.jpg" />
            <img src="slide3.jpg" />
          </div>
          <section class="content-wrapper">
          <!-- website content goes here -->
          </section>  


Css: Place a rule in your css file to hide the slides until the document loads completely (this will avoid the images flash at the begining)

          #screenslider{ display: none; } 
          
Js: Implement in your js file (main.js) the use of screenslider to your sliders wrapper

           (function($){
            $(window).load(function(){    
                $('#screenslider').screenslider({
                  pauseTime: 3000,
                  speed: 50 //between 0 and 100
                });   
            })
          })(jQuery);

Send your comments to: juanjo2988@gmail.com 
find me at http://mx.linkedin.com/in/juanjo2988/
