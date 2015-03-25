// JavaScript Document
/* dis/en able scroll */

// left: 37, up: 38, right: 39, down: 40,
// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
var keys = [37, 38, 39, 40];

function preventDefault(e) {
  e = e || window.event;
  if (e.preventDefault)
      e.preventDefault();
  e.returnValue = false;  
}

function keydown(e) {
    for (var i = keys.length; i--;) {
        if (e.keyCode === keys[i]) {
            preventDefault(e);
            return;
        }
    }
}

function wheel(e) {
  preventDefault(e);
}

function disable_scroll() {
  if (window.addEventListener) {
      window.addEventListener('DOMMouseScroll', wheel, false);
  }
  window.onmousewheel = document.onmousewheel = wheel;
  document.onkeydown = keydown;
}

function enable_scroll() {
    if (window.removeEventListener) {
        window.removeEventListener('DOMMouseScroll', wheel, false);
    }
    window.onmousewheel = document.onmousewheel = document.onkeydown = null;  
}


/* for open form!*/
$(document).ready(function(){

$('#sign-in').click(function(){
		
	      $('#sign').removeClass('fadeOutUpBig').addClass('fadeInDownBig');
		  $('#sign').css('display','block');
		  $('.modal-bg').fadeIn(500);
	});
	});
	
$(document).ready(function(){

$('#sign-out').click(function(){
	
		  $('#register').removeClass('fadeOutUpBig').addClass('fadeInDownBig');
		  $('#register').css('display','block');
		  $('.modal-bg').fadeIn(500);
	});
	});


/* for close form */
$(document).ready(function(){

		     $('#close-reg').click(function(){
			 $('.modal-bg').fadeOut(500);		
			 $('#register').removeClass('fadeInDownBig').addClass('fadeOutUpBig');
		  return false;
		})
});

$(document).ready(function(){

			 $('#close-sign').click(function(){
			 $('.modal-bg').fadeOut(500);
			 $('#sign').removeClass('fadeInDownBig').addClass('fadeOutUpBig');	
		  return false;
		})
});


