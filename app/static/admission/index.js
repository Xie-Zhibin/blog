var canSumb = false;
var ajax = function(method, url, cb, data, dataType) {
    var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
    xhr.open(method.toUpperCase(), url, true);
    if (method.toLowerCase() == 'get') {
        xhr.send(null)
    } else {
        var contentType = 'application/json';
        if (dataType) {
            if (dataType.toLowerCase() == 'json') {
                contentType = 'application/json'
            }
        };
        xhr.setRequestHeader("Content-type", contentType);
        xhr.send(data)
    };
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 500 || xhr.status === 404) {
                window.location.href = '/static/html/errorPages/404.html'
            };
            if (xhr.status === 200) {
                cb(xhr.responseText)
            }
        }
    }
};
var qClass = function(css) {
    return document.querySelector(css)
};
var testSumb = function() {
    if (qClass('.zkzh').value.length == 10 && qClass('.name-in').value.length != 0) {
        canSumb = true;
        return true
    };
    if (qClass('.zkzh').value.length != 10) {
        qClass('.zkzhErr').style.display = 'block';
        canSumb = false;
        return false
    };
    if (qClass('.name-in').value.length == 0) {
        qClass('.nameErr').style.display = 'block';
        canSumb = false;
        return false
    }
};
var useMsg = function(data) {
    var queryData = JSON.parse(data);
    if (queryData.status === 1) {
        qClass('.aftermsg').style.display = 'block';
        qClass('.query').style.display = 'none';
        qClass('.footer').style.display = 'none';
        var vm1 = new Vue({
            el: '#afmsg',
            data: queryData.data
        })
    } else {
            qClass('.errMsg-span').innerHTML = queryData.message;
            qClass('.errMsg').style.visibility = 'visible';
            back();
            canSumb = false;
        }
    };
var testZkzh = function() {
    if (qClass('.zkzh').value.length != 10) {
        qClass('.zkzhErr').style.display = 'block';
        canSumb = false
    } else {
        qClass('.zkzhErr').style.display = 'none';
        if (qClass('.name-in').value.length != 0) {
            canSumb = true
        }
    }
};
var testName = function() {
    if (qClass('.name-in').value.length == 0) {
        qClass('.nameErr').style.display = 'block';
        canSumb = false
    } else {
        qClass('.nameErr').style.display = 'none';
        if (qClass('.zkzh').value.length == 10) {
            canSumb = true
        }
    }
};
var query = function() {
    testSumb();
    if (canSumb) {
        qClass('.subm1 span').innerHTML = '正在查询...';
        var data = {
            sfzh: qClass('.name-in').value,
            code: qClass('.zkzh').value
        }
        var queryData = JSON.stringify(data);
        ajax('post', '/api/admission', useMsg, queryData)
    }
};
var back = function () {
    qClass('.query').style.display = 'block';
    qClass('.aftermsg').style.display = 'none';
    qClass('.footer').style.display = "block";
    qClass('.subm1 span').innerHTML = '查询';
};
qClass('.zkzh').addEventListener('blur', testZkzh, false);
qClass('.name-in').addEventListener('blur', testName, false);
qClass('.subm1').addEventListener('click', query, false);
qClass('.subm2').addEventListener('click', back, false);
