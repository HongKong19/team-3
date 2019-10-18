$(".thumb").mouseenter(function() {
	// if ($(this).find(".name").position().top > 40) {
		$(this).find(".white").transition({opacity: 0.8}, 600, 'snap')
		$(this).find(".name").transition({y:-40, opacity: 1}, 500, 'snap')
		$(this).find(".part").transition({y:-30, opacity: 1, delay: 100}, 450, 'snap')
		$(this).find(".description").transition({y:-20, opacity: 1, delay: 200}, 400, 'snap')
	// }
})

$(".thumb").mouseleave(function() {
	// if ($(this).find(".name").position().top < 40) {
		$(this).find(".white").transition({opacity: 0}, 600, 'snap')
		$(this).find(".description").transition({y:0, opacity: 0}, 500, 'snap')
		$(this).find(".part").transition({y:0, opacity: 0, delay: 100}, 450, 'snap')
		$(this).find(".name").transition({y:0, opacity: 0, delay: 200}, 400, 'snap')
	// }
})

$("#down").click(function() {
    $('html,body').animate({scrollTop:$("#muse-holistic").offset().top - 120}, 500)
})

var video_holistic = false
var video_hybrid = false
var video_multi = false

$(document).scroll(function() {
    if($("video#holistic").is(':onScreen')) {
        if (!video_holistic) {
        	video_holistic = true
        	$("video#holistic").get(0).play()
        }
    }

    if($("video#hybrid").is(':onScreen')) {
        if (!video_hybrid) {
        	video_hybrid = true
        	$("video#hybrid").get(0).play()
        }
    }

    if($("video#multi").is(':onScreen')) {
        if (!video_multi) {
        	video_multi = true
        	$("video#multi").get(0).play()
        }
    }
})

$("img").tooltip({
    "placement": "auto",
    "content":"html"
})
