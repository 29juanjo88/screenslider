/* http://www.juanjos.tk/screenslider/ screenslider created by juanjo */
(function ( $ ) {
  function ScreenSlider(selector, options) {
    tss = this;
    tss.selector = selector;
    var defaults = { pauseTime: 5000, speed: 90 }; 
    var options = $.extend({}, defaults, options); 
    tss.timeToSlide = options['pauseTime'];
    this.speed = function(){
      var speed = 100 - options['speed'];
      return tss.windowWidth() / speed;
    } 
    this.slides = function(){
      return tss.selector.find('img');
    }
    this.animate = function(){
      animationInterval = setInterval(function(){
          tss.animateSlide();
        },tss.timeToSlide);      
      $(window).focus(function () {
        clearInterval(animationInterval);        
        animationInterval = setInterval(function(){
          tss.animateSlide();
        },tss.timeToSlide);
      }).blur(function () {
        clearInterval(animationInterval);
      });
    }
    this.animateSlide = function(){
      var i = tss.speed();    
      (function moveSlides(){
       setTimeout(function(){
        tss.slides().each(function(){
          currentPos = $(this).position();    
          $(this).css('left', (currentPos.left - tss.speed())+'px')
        });
        i = i + tss.speed();
        if(i <= tss.windowWidth()){
          moveSlides();
        }else{
          tss.slides().first().appendTo(tss.selector)
          tss.fixPositions();
        }
      },2);
     })();
   }
   this.fixPositions = function(){
     itemNumber = 0;
     tss.slides().each(function(){
      $(this).css('left',(tss.windowWidth() * itemNumber));
      itemNumber++;
    });
   }
   this.windowWidth = function(){
    return tss.selector.width();
  }
  this.fixSize = function(){
    if(tss.windowWidth() > tss.selector.height()){
      tss.slides().css('width','100%');
      tss.slides().css('height','auto');
    }else{
      tss.slides().css('width','auto');
      tss.slides().css('height','100%');
    }
    if(tss.slides().first().height() < tss.selector.height()){
      tss.slides().css('height','100%');
    }
    tss.fixPositions();
  }
  window.onresize = function(){
    setTimeout(function(){
      tss.fixSize();
    },100)
  }
  tss.fixSize();
  tss.animate();
}
$.fn.screenslider = function(options){
  return this.each(function() {
    $(this).addClass('screenslider');
    new ScreenSlider($(this), options); 
    $(this).show();
  });
}
}( jQuery ));