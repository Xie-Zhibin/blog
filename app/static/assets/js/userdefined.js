//index
function cover() {
    //get the two new articles for cover
    var xmlhttp;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = xmlhttp.responseText;
            var json_data = JSON.parse(data);
            var source = $("#new_articles").html();
            var templat = Handlebars.compile(source);
            var context = { "article": json_data.data };
            var html = templat(context)
            $("#render_1").html(html)
        }
    }
    xmlhttp.open("GET", "/api/index", true);
    xmlhttp.send();
}


function newestArts() {
    //get id of two newest article of coding or others
    var xmlhttp;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = xmlhttp.responseText;
            var json_data = JSON.parse(data);
            var coding = json_data.data.coding;
            var others = json_data.data.others;
            document.getElementById("coding").href = "/static/coding.html?id=" + coding;
            document.getElementById("others").href = "/static/others.html?id=" + others;
        }
    }
    xmlhttp.open("GET", "/api/newestarts", true);
    xmlhttp.send();
}


//iframe
function getArt(path) {
    //get article for iframe
    var arg = location.search;
    var id = arg.split("=")[1] + ".html";
    document.getElementById("external-frame").src = path + id;
}

function setIframeHeight() {
    //auto adjust the height of iframe
    var iframe = document.getElementById('external-frame');
    if (iframe) {
        var iframeWin = iframe.contentWindow || iframe.contentDocument.parentWindow;
        if (iframeWin.document.body) {
            iframe.height = iframeWin.document.documentElement.scrollHeight || iframeWin.document.body.scrollHeight;
        }
        document.getElementById("loading").style.display="none";
    }
};

window.onload = function () {
setIframeHeight();
};

function unfload() {
    //to unfload div of iframe
    var fload_butt = document.getElementById("section");
    fload_butt.style.height = "100%";
    document.getElementById("unfload").style.display = "none";
    document.getElementById("fload").style.display = "inline-block";
}

function fload() {
    //to fload div of iframe
    var unfload_butt = document.getElementById("section");
    unfload_butt.style.height = 300 + "px";
    document.getElementById("unfload").style.display = "inline-block";
    document.getElementById("fload").style.display = "none";
}


//article list
function artList(args) {
    //function for get the title,id,type,time of articles to make a list
    var xmlhttp;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = xmlhttp.responseText;
            var json_data = JSON.parse(data);
            var source = $("#new_arts").html();
            var templat = Handlebars.compile(source);
            var context = { "arts": json_data.data };
            var html = templat(context)
            $("#render_2").html(html)
        }
    }
    xmlhttp.open("GET", "/api/getarts?" + args, true);
    xmlhttp.send();
}


//number of article
function num(type){
    //get number of article
    var xmlhttp;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = xmlhttp.responseText;
            var json_data = JSON.parse(data);
            var num = json_data.data;
            var coding = document.getElementById("coding_num");
            var others = document.getElementById("others_num");
            var all = document.getElementById("all_num");
            if (coding){
                coding.innerHTML = "(共" + num.coding + "篇)";
            }
            if (others){
                others.innerHTML = "(共" + num.others + "篇)";
            }
            if (all){
                all.innerHTML = "(共" + num.all + "篇)";
            }
        }
    }
    xmlhttp.open("GET", "/api/sum?" + type, true);
    xmlhttp.send();
}


//greeting
function greeting() {
    var xmlhttp;
    var hour;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = xmlhttp.responseText;
            var json_data = JSON.parse(data);
            hour = json_data.hours;
        }
        var msg;
        if (hour) {
            if (hour < 6) {
                msg = "Hi, 凌晨好！"
            } else if (hour < 9) {
                msg = "Hi, 早上好！"
            } else if (hour < 12) {
                msg = "Hi, 上午好！"
            } else if (hour < 14) {
                msg = "Hi, 中午好！"
            } else if (hour < 17) {
                msg = "Hi, 下午好！"
            } else if (hour < 19) {
                msg = "Hi, 傍晚好！"
            } else {
                msg = "Hi, 晚上好！"
            }
        } else {
            msg = "welcome!"
        }
        document.getElementById('welcome').innerHTML = msg;
    }
    xmlhttp.open("GET", "/api/time", true);
    xmlhttp.send();
    return hour;
}

//all articles
function allarts() {
    //get the two new articles for allarts
    var xmlhttp;
    if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = xmlhttp.responseText;
            var json_data = JSON.parse(data);
            var source = $("#insertAllArts").html();
            var templat = Handlebars.compile(source);
            var context = { "article": json_data.data };
            var html = templat(context)
            $("#allArticles").html(html)
        }
    }
    xmlhttp.open("GET", "/api/allarts", true);
    xmlhttp.send();
}