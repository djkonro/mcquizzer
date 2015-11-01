function set_timer(end_time, pos) {

	var d = Date.parse(new Date());
	var ms = (Date.parse(end_time) - d);
	var s = ms/1000;
	
	var th = Math.floor((s/3600));
	var tm = Math.floor((s%3600)/60);
	var ts = ((s%3600)%60);
	
	var sth = '';
	var stm = '';
	var sts = '';
	
	if(th >= 1){
		sth = ''+th+'h:'
	}else{
		sth = '00h:'
	}
	
	if(tm >= 1){
		stm = ''+tm+'m:'
	}else{
		stm = '00m:'
	}
	
	if(ts >= 1){
		sts = ''+ts+'s'
	}else{
		sts = '00s'
	}

	document.getElementById(pos).innerHTML  = sth+stm+sts;
	setTimeout(function() {set_timer(end_time, pos)}, 1000);
	
}

function set_time(qid, qtime){	
	
	var start = new Date();
	qtime = qtime * 60 * 1000;
	var end = Date.parse(start) + qtime;
	end = new Date(end);
	$.ajax({type: 'POST',
                url: '/set_date/'+qid+'/',                            // some data url
                data: {start: start.toString(), end : end.toString()},       // some params  
                success: function () {                  // callback
                     
                    },   
    			failure: function() { 
        			alert('Got an error dude');
    		},         
      });
      
      return end;
}   
