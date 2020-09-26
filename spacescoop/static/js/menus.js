$(document).ready(function(){

    $('#laguage_selector').mouseover(function() {
        // .position() uses position relative to the offset parent, 
        // so it supports position: relative parent elements
        var pos = $(this).position();

        // .outerWidth() takes into account border and padding.
        var height = $(this).outerHeight();
        var width = $(this).outerWidth();

        //show the menu directly over the placeholder
        $('#languages_menu').css({
            position: 'absolute',
            top: pos.top + + 'px',
            left: (-width/2) + 'px'
        }).show();
    });


    $(function() {
        var $oe_menu        = $('#languages_bar');
        var $oe_menu_items  = $oe_menu.children('li');
    
        $oe_menu_items.bind('mouseenter',function(){
            var $this = $(this);
            if ($this.children('div').length) {
                $this.addClass('slided selected');
            }
            $oe_menu_items.not('.slided').children('div').hide(); // for menu items that do not have a submenu
            $this.children('div').css('z-index','9999').stop(true,true).slideDown(200,function(){
                $oe_menu_items.not('.slided').children('div').hide();
                $this.removeClass('slided');
            });
        }).bind('mouseleave',function(){
            var $this = $(this);
            $this.removeClass('selected').children('div').css('z-index','1');
        });
    
        $oe_menu.bind('mouseenter',function(){
            var $this = $(this);
            $this.addClass('hovered');
        }).bind('mouseleave',function(){
            var $this = $(this);
            $this.removeClass('hovered');
            $oe_menu_items.children('div').hide();
        })
    });


	// social sharing
	$('#twitter').sharrre({
		share: {
			twitter: false
		},
		enableHover: false,
		enableTracking: true,
		// buttons: { twitter: {via: '_JulienH'}},
		click: function(api, options){
			// api.simulateClick();
			api.openPopup('twitter');
		}
	});
	$('#facebook').sharrre({
		share: {
			facebook: false
		},
		enableHover: false,
		enableTracking: true,
		click: function(api, options){
			// api.simulateClick();
			api.openPopup('facebook');
		}
	});
	$('#pinterest').sharrre({
		share: {
			pinterest: false
		},
		enableHover: false,
		enableTracking: true,
		click: function(api, options){
			// api.simulateClick();
			api.openPopup('pinterest');
		}
	});
});