var sliderMin = 0;
var sliderMax = 20;
var sliderStep = 1;
var sliderValue = sliderMax/2;
var commandID = 0;

// javascriptからcssを呼ぶ
// webiopi.cssが上書き優先されるのを防ぐため
function applyCustomClass(custom_css){
	var head = document.getElementsByTagName('head')[0];
	var style = document.createElement('link');
	style.rel = "stylesheet";
	style.type = "text/css";
	style.href = custom_css;
	head.appendChild(style);
}

function initialize_webiopi(){
	applyCustomClass('../css/jquery-ui.min.css')
	applyCustomClass('../css/styles.css')
	webiopi().refreshGPIO(false);
}

$(function(){
	var panSliderHandler = function(e, ui){
		var ratio = ui.value/sliderMax;
		webiopi().callMacro("setHwPWMforPan", [ratio, commandID++]);
	};

	$("#pan-slider").slider({
		min: sliderMin,
		max: sliderMax,
		step: sliderStep,
		value: sliderValue,
		slide: panSliderHandler
	});

});
