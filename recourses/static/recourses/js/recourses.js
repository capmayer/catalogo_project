$(document).ready( function() {

			    $("#filter-bar li").click(function(){
				    $("#filter-bar li").removeClass("active");
				    $(this).addClass("active");
				    $("#filter-bar").removeClass().addClass($(this).attr("data-target"));

			    });

			})
