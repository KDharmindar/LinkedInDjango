
$(function() {
    
    $('.campaignsteps-row>div').formset({
        // For inline formsets, be sure to set the prefix, as the default prefix
        // ('form') isn't correct.
        // Django appears to generate the prefix from the lowercase plural
        // name of the related model, with camel-case converted to underscores.
        prefix: 'stepmessages',
        addText: 'Add another message',          // Text for the add link
        deleteText: 'Remove this message',            // Text for the delete link
        addCssClass: 'add-row btn btn-primary',          // CSS class applied to the add link
        deleteCssClass: 'delete-row btn btn-danger mb-xl',    // CSS class applied to the delete link
    });
    
    
    $('.slider').click(function(e){
    	
    	var that = $(e.target).prev();
    	that.click();
    	console.log('checked:', that.is(":checked"));
    	var url = window.location.href;
    	var data = "active=" + (that.is(":checked") ? 1 : 0);
    	
    	$.get(url+"/active?"+data).done(function(res){
    		$('body').find('.switch_campaign').each(function(ex){        		
        		if (this !== that){
        			$(this).trigger('click');
        		}
        	});
    	});
    	
    	
    	
    });
    
    $('.btn-save').click(function(e){
    	e.preventDefault();
    	var that = $(this);
    	var form = that.closest('form');
    	var data = form.serialize();
    	$.post(form.attr('action'), data).done(function(res){
    		res = $.parseJSON(res);
    		console.log('resutl:', res);
    		var alertbox = $('.alert-box');
    		if (res.ok) {
    			alertbox.html('Message has been saved successfully!');
    			alertbox.addClass('text-success').removeClass('text-danger');
    			return;
    		}
    		if ( res.error){
    			var html = "";
    			$.each( res.error, function( i, obj ) {
    				
    				var key = Object.keys(obj);
    				if (obj[key])
    					html+=  key + ": " + obj[key] + "<br/>";
    			});
    			alertbox.html( html );
    			alertbox.removeClass('text-success').addClass('text-danger')
    		}
    	});
    });
    
    $("a[data-click='removeCampaign']").click(function(e) {
		e.preventDefault();
		$('#confirm_dialog>div').modal('show');
	});
    
    $('body').on('click', '#confirm_dialog >div #confirm_button', function(e){
    	
    	var url = window.location.href;
    	var data = $('body').find('form[name="campaign"]').serialize();        	
    	$.post(url+"/delete", data).done(function(res){
    		var to = url.lastIndexOf('/');
        	to = to == -1 ? url.length : to + 1;
        	var url2 = url.substring(0, to);
    		window.location = url2;
    	});
    	
    });
    
});