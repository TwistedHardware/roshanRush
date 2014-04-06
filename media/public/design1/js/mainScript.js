home=true;
function openPage(page)
{
	if (page=="home")
	{
		setLayoutHome(true);
		home=true;
		
	}
	else
	{
		if(! home)
		{
			setLayoutHome(false);
			setTimeout(function(){setLayoutContent();},300);
		}
		else
		{
			setLayoutContent();
		}
		home=false;
		
		
		$("#" + page)
		.css({
			"overflow": "visible",
			"height": "auto",
			"bottom": "57px",
			"z-index": "1",
		})
		.animate({
			"top": "45px",
		},
		300,
		"swing"
		);
	}

}

function setLayoutHome(enlargeLogo)
{
	if(enlargeLogo)
	{
		$("#largeLogo").animate({
			"bottom": "50%",
		},
		300,
		"swing"
		);
		
		$("#logoImage").animate({
			"width": "778px",
			"height": "auto",
			"margin-left": "auto",
			"margin-right": "auto"
		},
		300,
		"swing"
		);
	}
	
	$("#topPanel").animate({
		"bottom": "57px",
		"height": "auto"
	},
	300,
	"swing"
	);
	
	$(".ContentArea")
	.css({
		"overflow": "hidden",
		"bottom": "auto",
		"height": "5px",
		"z-index": "-1",
	})
	.animate({
		"top": "0px",
	},
	300,
	"swing"
	);
	
	
}

function setLayoutContent(page)
{
	$("#topPanel").animate({
		"bottom": "auto",
		"height": "45px"
	},
	500,
	"swing"
	);
	
	$("#largeLogo").animate({
		"bottom": "0px"
	},
	500,
	"swing"
	);
	
	$("#logoImage").animate({
		"width": "166px",
		"height": "auto",
		"left": "5px",
		"margin-left": "0px",
		"margin-right": "0px"
	},
	500,
	"swing"
	);
}

function OpenInNewTab(url )
{
	console.log('test');
	var win=window.open(url, '_blank');
	win.focus();
}